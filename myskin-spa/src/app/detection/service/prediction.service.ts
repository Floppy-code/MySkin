import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { PredictionEncodedFile } from 'src/app/core/model/prediction-encoded-file';
import { PredictionResult } from 'src/app/core/model/prediction-result';

@Injectable({
  providedIn: 'root',
})
export class PredictionService {
  private backendUrl: string = '127.0.0.1:5000'; //Backend API base URL

  predictionResult$: Observable<PredictionResult>;

  constructor(private httpClient: HttpClient) {
    this.predictionResult$ = of({ data: 'asedawe' });
  }

  predict(image: File): Observable<PredictionResult> {
    let encodedImage: PredictionEncodedFile = this.encodeFileToBase64(image);

    return this.httpClient.post<PredictionResult>(
      this.backendUrl + '/predict',
      encodedImage
    );
  }

  private encodeFileToBase64(file: File): PredictionEncodedFile {
    let encoded: PredictionEncodedFile = { Base64EncodedImage: '' };
    let fileReader: FileReader = new FileReader();

    fileReader.readAsDataURL(file);
    fileReader.onload = (e) => {
      encoded.Base64EncodedImage = e.target?.result;
      console.log('Encoded image:', encoded);
    };

    fileReader.onerror = (e) => {
      console.error('FileReader error: ', e);
      return null;
    };

    return encoded;
  }
}
