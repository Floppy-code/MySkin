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

  predictionResult$?: Observable<PredictionResult>;

  constructor(private httpClient: HttpClient) {}

  public predict(image: File): void {
    //Encode image to Base64.
    let encodedImage: PredictionEncodedFile = this.encodeFileToBase64(image);

    // //Send image to backend and await response.
    // return this.httpClient.post<PredictionResult>(
    //   this.backendUrl + '/predict',
    //   encodedImage
    // );

    //Mocked output
    this.predictionResult$ = of({ confidence: 0.6, type: 'blk' });
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
