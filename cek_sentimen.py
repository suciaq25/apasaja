print("1. Memulai script...")
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # Menghilangkan log berlebih dari TF

print("2. Mengimpor library (ini mungkin memakan waktu)...")
try:
    import tensorflow as tf
    import pickle
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    print("3. Library berhasil diimpor.")
except Exception as e:
    print(f"Error saat impor library: {e}")

def jalankan():
    try:
        print("4. Mencoba memuat model 'model_rnn.h5'...")
        model = tf.keras.models.load_model('model_rnn.h5')
        
        print("5. Mencoba memuat tokenizer...")
        with open('tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)
        
        print("\n--- Sistem Siap ---")
        teks = input("Masukkan ulasan untuk diuji: ")
        
        # Preprocessing
        seq = tokenizer.texts_to_sequences([teks])
        pad = pad_sequences(seq, maxlen=100, padding='post')
        
        # Prediksi
        res = model.predict(pad, verbose=0)[0][0]
        label = "POSITIF" if res >= 0.5 else "NEGATIF"
        
        print(f"\nHasil Analisis:")
        print(f"Sentimen: {label}")
        print(f"Skor: {res:.4f}")
        
    except Exception as e:
        print(f"\nTerjadi Kesalahan: {e}")

if __name__ == "__main__":
    jalankan()