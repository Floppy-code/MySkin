import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class CategoryDescriptionService {
  
  private categoryDesciptions: { [id: string]: string } = {
    akiec:
      'This category includes precancerous lesions that develop on sun-exposed areas of the skin, such as the face and hands. They are typically characterized by rough, scaly patches.',
    bcc: 'This category includes non-melanoma skin cancers that arise from the basal cells, which are located in the deepest layer of the skin. Basal cell carcinoma is the most common form of skin cancer.',
    bkl: 'This category includes benign skin lesions that are similar in appearance to actinic keratoses. However, they do not have the same potential to develop into skin cancer.',
    df: 'This category includes benign skin tumors that arise from fibroblasts, which are cells that produce collagen. Dermatofibromas are typically firm, raised, and reddish-brown in color.',
    mel: 'This category includes malignant skin tumors that arise from melanocytes. Melanoma is one of the most deadly forms of skin cancer, and early detection is crucial for successful treatment.',
    nv: 'This category includes benign, typically pigmented skin lesions that are commonly referred to as moles. They are formed by an overgrowth of melanocytes, the cells that produce pigment in the skin.',
    vasc: 'This category includes a variety of benign skin lesions that involve blood vessels. Examples include hemangiomas, which are clusters of blood vessels that form a red or purple bump on the skin, and angiokeratomas, which are raised, dark red or purple lesions that are composed of dilated blood vessels.',
  };

  constructor() {}

  public GetCategoryDescription(category: string): string {
    return this.categoryDesciptions[category];
  }
}
