import { useState } from 'react';
import React from 'react';

import styles from './MainQr.module.css'

export function MainQr() {
    const [link, setLink] = useState('');
    const [, setQrCodeImage] = useState<string | null>(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => { 
        e.preventDefault();
        setLoading(true);

        try{
            // Cria o objeto formData
            const formData = new FormData();

            // O primeiro argumento 'data' deve ser EXATAMENTE o nome que o Flask espera no request.form['data']
            formData.append('data', link);

            // Faz a requisição POST para o backend Flask
            const response = await fetch('http://127.0.0.1:5000/api/qrgen', {
                method: 'POST',
                body: formData,
                // IMPORTANTE: Não defina 'Content-Type' manualmente aqui. 
                // O fetch fará isso sozinho para lidar com o boundary do form-data.
            });

            if (!response.ok){
                throw new Error('Erro na geração do QR Code');
            }

            // Transforma a resposta em um Blob (arquivo)
            const imageBlob = await response.blob();
            // Cria uma URL temporária para esse arquivo
            const imageUrl = URL.createObjectURL(imageBlob);
            // Cria um elemento <a> (link) temporário
            const tempLink = document.createElement('a');
            tempLink.href = imageUrl;

            // Define o nome do arquivo que será baixado
            tempLink.download = 'qrcode.png'

            // Adiciona ao corpo do documento (necessário para o Firefox), clica e remove
            document.body.appendChild(tempLink);
            tempLink.click();
            document.body.removeChild(tempLink);

            // Limpa a URL da memória para não gastar recursos
            URL.revokeObjectURL(imageUrl)

            setQrCodeImage(imageUrl);

            } catch (error) {
                console.error('Erro: ', error);
                alert("Falha ao conectar com a API");
            } finally {
                setLoading(false);
            }

        };


    return (
        <main className={styles.mainContainer}>
            <div className={styles.mainAbove}>
                <p className={styles.mainSubtitleAbove}>Seu QR Code Fácil</p>
                <h1 className={styles.mainTitleAbove}>QR Generator</h1>
                <p className={styles.mainTextAbove}>Gere QR Code de forma simples e gratuíta no seu navegador.</p>
            </div>

                <form className={styles.mainBelow} onSubmit={handleSubmit}>
                    <input className={styles.mainInputTextBelow} 
                        type="text" 
                        placeholder='Cole o seu link aqui'
                        value={link}
                        onChange={(e) => setLink(e.target.value)}
                        />

                        <button className={styles.mainButtonBelow} type="submit" disabled={loading}>{loading ?  'Baixando...' : 'Generate'}</button>
                </form>

        </main>
    )
};

export default MainQr; 