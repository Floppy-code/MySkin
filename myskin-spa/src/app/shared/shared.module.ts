import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NavBarComponent } from './component/nav-bar/nav-bar.component';

import {MatIconModule} from '@angular/material/icon';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import {MatMenuModule} from '@angular/material/menu';
import {MatCommonModule} from '@angular/material/core';


@NgModule({
  declarations: [
    NavBarComponent,
    
  ],
  imports: [
    CommonModule,
    MatCommonModule,
    MatIconModule,
    MatToolbarModule,
    MatButtonModule,
    MatMenuModule,
  ],
  exports: [
    NavBarComponent
  ]
})
export class SharedModule { }
