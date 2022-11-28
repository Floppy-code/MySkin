import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { WelcomeComponent } from './component/welcome/welcome.component';
import { PageNotFoundComponent } from './component/page-not-found/page-not-found.component';

import { MatCommonModule } from '@angular/material/core';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { MatDividerModule } from '@angular/material/divider';

@NgModule({
  declarations: [WelcomeComponent, PageNotFoundComponent],
  imports: [
    CommonModule,
    MatCommonModule,
    MatCardModule,
    MatButtonModule,
    MatDividerModule,
  ],
})
export class CoreModule {}
