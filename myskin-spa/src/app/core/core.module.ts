import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { WelcomeComponent } from './component/welcome/welcome.component';
import { PageNotFoundComponent } from './component/page-not-found/page-not-found.component';
import { SharedModule } from '../shared/shared.module';



@NgModule({
  declarations: [
    WelcomeComponent,
    PageNotFoundComponent
  ],
  imports: [
    CommonModule,
    SharedModule,
  ]
})
export class CoreModule { }
