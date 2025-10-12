import torch

# 假设 logits 形状为 [2, vocab_size=10]
logits = torch.randn(2, 10)  # batch_size=2, vocab_size=10
print(logits)
# 假设 self.label_words_ids 形状为 [2, 4, 2]
label_words_ids = torch.tensor([
    [[1, 3], [4, 2], [6, 7], [8, 9]],  # 第一个样本的索引
    [[2, 5], [1, 0], [7, 8], [3, 6]]   # 第二个样本的索引
])  # 形状 [2, 4, 2]

# 进行索引
label_words_logits = logits[:, label_words_ids]  # 形状 [2, 4, 2]
print(label_words_logits)
print("logits shape:", logits.shape)  # [2, 10]
print("label_words_ids shape:", label_words_ids.shape)  # [2, 4, 2]
print("label_words_logits shape:", label_words_logits.shape)  # [2, 2, 4, 2]

