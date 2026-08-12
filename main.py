import textwrap

def simple_tokenize(text):
    """
    A very simplified tokenizer for demonstration purposes.
    Splits text into words and common punctuation as tokens.
    Real LLMs use more complex subword tokenization (e.g., BPE).
    """
    tokens = []
    # Split by whitespace first
    for word in text.split():
        # Simple heuristic: if a word ends with common punctuation, separate it
        if len(word) > 1 and word[-1] in '.,!?;:':
            tokens.append(word[:-1])
            tokens.append(word[-1])
        else:
            tokens.append(word)
    return tokens

def simulate_llm_processing(prompt_text, max_context_tokens):
    """
    Simulates an LLM processing a prompt within a limited context window.
    This function illustrates the article's main concept: how LLMs handle
    prompts that exceed their token limit.
    """
    print(f"\n--- Simulating LLM Processing ---")
    print(f"Original Prompt (length: {len(prompt_text)} chars):")
    print(textwrap.fill(prompt_text, width=70))

    # Convert the prompt into a list of "tokens"
    # This is where the article's core concept of 'token' comes into play.
    prompt_tokens = simple_tokenize(prompt_text)
    print(f"\nPrompt Token Count (simplified): {len(prompt_tokens)}")
    print(f"Max Context Window (tokens): {max_context_tokens}")

    if len(prompt_tokens) > max_context_tokens:
        # This demonstrates the article's main point: truncation due to context window limit.
        truncated_tokens = prompt_tokens[:max_context_tokens]
        processed_text = " ".join(truncated_tokens)
        print(f"\nPrompt EXCEEDS context window. Truncating to {max_context_tokens} tokens.")
        print(f"Ignored tokens: {len(prompt_tokens) - max_context_tokens}")
        print(f"Processed Prompt (first {max_context_tokens} tokens):\n")
        print(textwrap.fill(processed_text + "... [rest of prompt ignored]", width=70))
        return processed_text + "..."
    else:
        # The prompt fits within the context window.
        processed_text = " ".join(prompt_tokens)
        print(f"\nPrompt FITS within context window. Processing full prompt.\n")
        print(f"Processed Prompt:\n")
        print(textwrap.fill(processed_text, width=70))
        return processed_text

# Define a simulated context window size (small for clear demonstration)
MAX_CONTEXT_TOKENS = 50

print("----------------------------------------------------------------------")
print("Demonstration of LLM Context Window and Token Truncation")
print("----------------------------------------------------------------------")

# --- Example 1: Short prompt (fits within context window) ---
short_prompt = (
    "Merhaba! Lütfen bana Büyük Dil Modelleri'nin (LLM'ler) temel özelliklerini "
    "ve bağlam penceresi kavramını kısaca açıklar mısın? "
    "Bu teknolojinin günlük hayatta nasıl kullanıldığına dair birkaç örnek de verirsen sevinirim."
)
print("\n### Scenario 1: Short Prompt (fits context window) ###")
simulate_llm_processing(short_prompt, MAX_CONTEXT_TOKENS)

# --- Example 2: Long prompt (exceeds context window) ---
long_prompt = (
    "Merhaba sevgili yapay zeka asistanı! Bugün sana oldukça detaylı bir görevim var. "
    "Lütfen aşağıdaki metni dikkatlice oku ve ana fikrini özetle. "
    "Ardından, metinde bahsedilen kavramları kullanarak yeni bir hikaye oluştur. "
    "Hikaye, bir uzay gemisinin bilinmeyen bir gezegene inişini ve mürettebatın orada karşılaştığı "
    "garip yaşam formlarını anlatmalı. Hikayenin sonunda, mürettebatın gezegenden ayrılma kararı "
    "vermesinin nedenlerini ve bu kararın sonuçlarını da belirt. "
    "Metin: Büyük Dil Modelleri (LLM'ler), milyarlarca parametreye sahip, devasa metin veri kümeleri "
    "üzerinde eğitilmiş yapay zeka sistemleridir. Bu modeller, insan dilini anlama, üretme ve işleme "
    "yeteneği sayesinde birçok alanda devrim yaratmıştır. Ancak, bu etkileyici yeteneklerin arkasında, "
    "modellerin çalışma prensiplerinden kaynaklanan bazı kısıtlamalar da bulunmaktadır. "
    "Bu kısıtlamaların başında 'bağlam penceresi' (context window) ve 'token' kavramları gelir. "
    "Bir LLM ile etkileşime girdiğinizde, aslında modele bir metin dizisi (prompt) gönderirsiniz "
    "ve model bu diziyi analiz eder. Modelin aynı anda işleyebileceği token sayısı sınırlıdır. "
    "Bu sınıra 'bağlam penceresi' denir. Eğer prompt bu pencereyi aşarsa, model prompt'un son kısımlarını "
    "göz ardı edebilir veya hiç işlemeyebilir. Bu durum, özellikle karmaşık görevlerde veya geniş bilgi "
    "setleriyle çalışırken ciddi bir hayal kırıklığına yol açabilir. "
    "Bu makalede, bu yaygın sorunun temel nedenlerini, nasıl tespit edileceğini ve bu durumun üstesinden "
    "gelmek için kullanabileceğiniz etkili stratejileri derinlemesine inceleyeceğiz. "
    "Amacımız, LLM'lerle daha verimli ve başarılı etkileşimler kurmanıza yardımcı olmaktır."
)
print("\n### Scenario 2: Long Prompt (exceeds context window) ###")
simulate_llm_processing(long_prompt, MAX_CONTEXT_TOKENS)

# --- Example 3: Very long prompt with specific instructions at the end ---
# This highlights how important instructions can be lost if they are at the end.
very_long_prompt = (
    "Bu çok uzun bir giriş metni. Amacımız, Büyük Dil Modelleri'nin (LLM'ler) "
    "sınırlı bağlam penceresi nedeniyle uzun komutların nasıl göz ardı edildiğini "
    "göstermek. Bu metin, çeşitli konuları ele alan anlamsız cümlelerle doldurulmuştur "
    "ki bağlam penceresini kolayca aşsın. Güneş sistemimizde sekiz gezegen bulunur ve Mars, "
    "Kızıl Gezegen olarak bilinir. Kediler ve köpekler popüler evcil hayvanlardır, ancak "
    "farklı davranışlara sahiptirler. Su, H2O formülüyle bilinen temel bir yaşam kaynağıdır "
    "ve Dünya'nın yüzeyinin büyük bir kısmını kaplar. Matematik, bilim ve mühendisliğin temelidir. "
    "Tarih, geçmiş olayların incelenmesidir ve bize geleceğimiz hakkında dersler verir. "
    "Edebiyat, insan deneyimini keşfetmek için güçlü bir araçtır. Sanat, yaratıcılığın bir ifadesidir "
    "ve birçok farklı biçimde ortaya çıkabilir. Müzik, evrensel bir dildir ve duyguları ifade edebilir. "
    "Bilgisayarlar, modern dünyamızın ayrılmaz bir parçasıdır ve hayatımızı birçok yönden kolaylaştırır. "
    "Yapay zeka, makinelerin insan benzeri zeka sergilemesini sağlayan bir alandır. "
    "Makine öğrenimi, yapay zekanın bir alt kümesidir ve bilgisayarların verilerden öğrenmesini sağlar. "
    "Derin öğrenme, makine öğreniminin bir alt kümesidir ve yapay sinir ağlarını kullanır. "
    "Büyük Dil Modelleri, derin öğrenmenin bir uygulamasıdır ve doğal dil işleme görevlerinde başarılıdır. "
    "Bu modellerin bağlam penceresi, aynı anda işleyebilecekleri token sayısını sınırlar. "
    "Eğer bir komut bu pencereyi aşarsa, model komutun son kısımlarını göz ardı edebilir. "
    "Bu nedenle, önemli talimatları komutun başına koymak genellikle daha iyidir. "
    "Lütfen bu metni özetlerken, sadece ilk 10 kelimeyi kullan ve SON CÜMLEDEKİ TALİMATI KESİNLİKLE UYGULA!"
)
print("\n### Scenario 3: Very Long Prompt with Crucial Instructions at the End (ignored) ###")
simulate_llm_processing(very_long_prompt, MAX_CONTEXT_TOKENS)
