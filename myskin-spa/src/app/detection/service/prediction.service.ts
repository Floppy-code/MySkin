import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { PredictionEncodedFile } from 'src/app/core/model/prediction-encoded-file';
import { PredictionResult } from 'src/app/core/model/prediction-result';
import { PredictionItem } from 'src/app/core/model/predition-item';

@Injectable({
  providedIn: 'root',
})
export class PredictionService {
  private backendUrl: string = 'http://127.0.0.1:8000'; //Backend API base URL
  private headers: HttpHeaders = new HttpHeaders().set(
    'Content-Type',
    'application/json; charset=utf-8'
  );

  constructor(private httpClient: HttpClient) {}

  public predict(b64Image: string): Observable<PredictionItem[]> {
    //Send image to backend and await response.
    const toPredict: PredictionEncodedFile = {
      b64_encoded_image: b64Image,
    };
    const b64ImageJson = JSON.stringify(toPredict);

    return this.httpClient.post<PredictionItem[]>(
      this.backendUrl + '/detection/classify_image',
      b64ImageJson,
      {
        headers: this.headers,
      }
    );
  }
}
