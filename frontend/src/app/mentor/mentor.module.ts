import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';

import { MentorPage } from './mentor/mentor.page';
import { MentorListingPage } from './mentor-listing/mentor-listing.page';
import { MentorDetailPage } from './mentor-detail/mentor-detail.page';

/*const routes: Routes = [

  {
    path: '',
    component: MentorPage
  }
];*/

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ReactiveFormsModule
  ],
  declarations: [MentorPage, MentorDetailPage, MentorListingPage]
})
export class MentorPageModule {}
