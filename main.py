import pandas as pd
df = pd.DataFrame(([1,2,3],[1,2,3]), index=list('ac'), columns=list('ABC'))
print(df.style.background_gradient('blues'))