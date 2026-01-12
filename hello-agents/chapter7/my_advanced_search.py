import os 
from typing import Optional, List, Dict, Any
from hello_agents import ToolRegistry 

class MyAdvancedSearchTool:
    """  
    自定义高级搜索工具类
    展示多源整合和智能选择的设计模式
    """

    def __init__(self):
        self.name = "my_advanced_search"
        self.description = "智能搜索工具，支持多个搜索源，自动选择最佳结果"
        self.search_sources = []
        self._setup_search_sources()

    def _setup_search_sources(self):
        """设置可用的搜索源"""
        # 检查Tavily可用性
        if api_key := os.getenv("TAVILY_API_KEY"):
            try:
                from tavily import TavilyClient
                self.tavily_client = TavilyClient(api_key=api_key)
                self.search_sources.append("tavily")
                print("Tavily搜索源已启用")
            except ImportError:
                print("⚠️ Tavily库未安装")

        # 检查SerpAPI可用性
        if api_key := os.getenv("SERPAPI_API_KEY"):
            try:
                import serpapi
                self.search_sources.append("serpapi")
                print("SerpAPI搜索源已启用")
            except ImportError:
                print("⚠️ SerpAPI库未安装")

        if self.search_sources:
            print(f"可用搜索源: {', '.join(self.search_sources)}")
        else:
            print("⚠️ 未检测到可用的搜索源,请配置环境变量")
        
    def search(self, query: str) -> str:
        """执行智能搜索"""
        if not query.strip():
            return "错误：搜索查询不能为空"

        # 检查是否有可用的搜索源
        if not self.search_sources:
            return """❌ 没有可用的搜索源，请配置以下API密钥之一:

1. Tavily API: 设置环境变量 TAVILY_API_KEY
获取地址: https://tavily.com/

2. SerpAPI: 设置环境变量 SERPAPI_API_KEY
获取地址: https://serpapi.com/

配置后重新运行程序。
"""

        print(f"开始智能搜索: {query}")

        # 尝试多个搜索源，返回最佳结果
        for source in self.search_sources:
            try:
                if source == "tavily":
                    result = self._search_with_tavily(query)
                    if result and "未找到" not in result:
                        return f"🔍 Tavily搜索结果:\n{result}"

                elif source == "serpapi":
                    result = self._search_with_serpapi(query)
                    if result and "未找到" not in result:
                        return f"🔍 SerpAPI搜索结果:\n{result}" 
                    
            except Exception as e:
                print(f"⚠️ 使用 {source} 搜索时出错: {str(e)}")
                continue

        return "所有搜索源都失败，请检查网络连接和API配置"

    def _search_with_tavily(self, query: str) -> str:
        """使用Tavily搜索"""
        response = self.tavily_client.search(query=query, max_results=3)

        if response.get('answer'):
            result = f"💡 AI直接答案:{response['answer']}\n\n"
        else:
            result = ""

        result += "🔗 相关结果:\n"
        for i, item in enumerate(response.get('results', [])[:3], 1):
            result += f"[{i}] {item.get('title', '')}\n"
            result += f"    {item.get('content', '')[:150]}...\n\n"

        return result

    def _search_with_serpapi(self, query: str) -> str:
        """使用SerpApi搜索"""
        import serpapi

        search = serpapi.GoogleSearch({
            "q": query,
            "api_key": os.getenv("SERPAPI_API_KEY"),
            "num": 3
        })

        results = search.get_dict()

        result = "🔗 Google搜索结果:\n"
        if "organic_results" in results:
            for i, res in enumerate(results["organic_results"][:3], 1):
                result += f"[{i}] {res.get('title', '')}\n"
                result += f"    {res.get('snippet', '')}\n\n"

        return result       
    
def create_advanced_search_registry() -> ToolRegistry:
    """创建包含高级搜索工具的注册表"""
    registry = ToolRegistry()
    advanced_search_tool = MyAdvancedSearchTool()
    registry.register_function(
        name = advanced_search_tool.name,
        description = advanced_search_tool.description,
        func = advanced_search_tool.search
    )

    return registry
