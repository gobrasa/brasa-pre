import { IonicModule } from '@ionic/angular';
import { RouterModule } from '@angular/router';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { TabsPageRoutingModule } from './tabs.router.module';

import { TabsPage } from './tabs.page';

import { MenteePageModule } from '../mentee/mentee.module';
import { MentorPageModule } from '../mentor/mentor.module';

@NgModule({
  imports: [
    IonicModule,
    CommonModule,
    FormsModule,
    TabsPageRoutingModule,
    MenteePageModule,
    MentorPageModule
  ],
  declarations: [TabsPage]
})
export class TabsPageModule {}
