---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "CustomerDirectDebitInitiation pain.008.001.12 "]
content_origin: "source-transcription"
---

# CustomerDirectDebitInitiation pain.008.001.12 

Source: [src-000173](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx). Locator: heading path Business Examples / CustomerDirectDebitInitiation pain.008.001.12 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P763** CustomerDirectDebitInitiation pain.008.001.12 

**P764** Narrative

**P765** On 2 June 2012, Virgay insurance company sends a CustomerDirectDebitInitiation message to its account servicer, AAAAUS29. AAAAUS29 offers a special service to Virgay, under agreement VERPA-1.

**P766** The direct debit initiation message contains two collection instructions from two different debtors.

**P767** The first direct debit instruction is for 1025 USD to be collected from account 123456, owned by debtor Jones and serviced by agent BBBBUS39. The mandate reference is VIRGAY123 and was signed by Jones on 13 July 2008. The last collection is due to take place on 13 July 2015. The payment is for a yearly life insurance fee.

**P768** The second direct debit instruction is for 985 USD to be collected from account 789101, owned by debtor Lee and serviced by agent CCCCUS27. This is a one-off direct debit which was notified to Lee on 8 June 2012, with reference VIRGAY2435/2012. The payment is for a car insurance premium.

**P769** The requested collection date for both collections is 13 July 2012 and charges related to the handling of the instruction will be shared between Virgay insurance company and the debtors.

**P770** Business Data

**P771** CustomerDirectDebitInitiation from Virgay to AAAAUS29:

[T28 - complete table](../tables/tbl-0028.md)

**P772** Message Instance

**P773** <CstmrDrctDbtInitn>

**P774** 	<GrpHdr>

**P775** 		<MsgId>CAVAY1234</MsgId>

**P776** 		<CreDtTm>2012-06-02T14:25:00</CreDtTm>

**P777** 		<NbOfTxs>2</NbOfTxs>

**P778** 		<CtrlSum>2010</CtrlSum>

**P779** 		<InitgPty>

**P780** 			<Nm>Virgay</Nm>

**P781** 			<PstlAdr>

**P782** 				<StrtNm>Virginia Lane</StrtNm>

**P783** 				<BldgNb>36</BldgNb>

**P784** 				<PstCd>NJ 07311</PstCd>

**P785** 				<TwnNm>Jersey City</TwnNm>

**P786** 				<Ctry>US</Ctry>

**P787** 			</PstlAdr>

**P788** 			<CtctDtls>

**P789** 				<Nm>J. Thompson</Nm>

**P790** 				<EmailAdr>Thompson@virgay.com</EmailAdr>

**P791** 			</CtctDtls>

**P792** 		</InitgPty>

**P793** 	</GrpHdr>

**P794** 	<PmtInf>

**P795** 		<PmtInfId>CAVAY/88683</PmtInfId>

**P796** 		<PmtMtd>DD</PmtMtd>

**P797** 		<BtchBookg>false</BtchBookg>

**P798** 		<ReqdColltnDt>2012-07-13</ReqdColltnDt>

**P799** 		<Cdtr>

**P800** 			<Nm>Virgay</Nm>

**P801** 			<PstlAdr>

**P802** 				<StrtNm>Virginia Lane</StrtNm>

**P803** 				<BldgNb>36</BldgNb>

**P804** 				<PstCd>NJ 07311</PstCd>

**P805** 				<TwnNm>Jersey City</TwnNm>

**P806** 				<Ctry>US</Ctry>

**P807** 			</PstlAdr>

**P808** 		</Cdtr>

**P809** 		<CdtrAcct>

**P810** 			<Id>

**P811** 				<Othr>

**P812** 					<Id>789123</Id>

**P813** 				</Othr>

**P814** 			</Id>

**P815** 		</CdtrAcct>

**P816** 		<CdtrAgt>

**P817** 			<FinInstnId>

**P818** 				<BICFI>AAAAUS29</BICFI>

**P819** 			</FinInstnId>

**P820** 		</CdtrAgt>

**P821** 		<DrctDbtTxInf>

**P822** 			<PmtId>

**P823** 				<EndToEndId>VA060327/0123</EndToEndId>

**P824** 			</PmtId>

**P825** 			<PmtTpInf>

**P826** 				<InstrPrty>NORM</InstrPrty>

**P827** 				<SvcLvl>

**P828** 					<Prtry>VERPA-1</Prtry>

**P829** 				</SvcLvl>

**P830** 				<SeqTp>RCUR</SeqTp>

**P831** 			</PmtTpInf>

**P832** 			<InstdAmt Ccy="USD">1025</InstdAmt>

**P833** 			<ChrgBr>SHAR</ChrgBr>

**P834** 			<DrctDbtTx>

**P835** 				<MndtRltdInf>

**P836** 					<MndtId>VIRGAY123</MndtId>

**P837** 					<DtOfSgntr>2008-07-13</DtOfSgntr>

**P838** 					<FnlColltnDt>2015-07-13</FnlColltnDt>

**P839** 					<Frqcy><Tp>YEAR</Tp></Frqcy>

**P840** 				</MndtRltdInf>

**P841** 			</DrctDbtTx>

**P842** 			<DbtrAgt>

**P843** 				<FinInstnId>

**P844** 					<BICFI>BBBBUS39</BICFI>

**P845** 				</FinInstnId>

**P846** 			</DbtrAgt>

**P847** 			<Dbtr>

**P848** 				<Nm>Jones</Nm>

**P849** 				<PstlAdr>

**P850** 					<StrtNm>Hudson Street</StrtNm>

**P851** 					<BldgNb>19</BldgNb>

**P852** 					<PstCd>NJ 07302</PstCd>

**P853** 					<TwnNm>Jersey City</TwnNm>

**P854** 					<Ctry>US</Ctry>

**P855** 				</PstlAdr>

**P856** 			</Dbtr>

**P857** 			<DbtrAcct>

**P858** 				<Id>

**P859** 					<Othr>

**P860** 						<Id>123456</Id>

**P861** 					</Othr>

**P862** 				</Id>

**P863** 			</DbtrAcct>

**P864** 			<Purp>

**P865** 				<Cd>LIFI</Cd>

**P866** 			</Purp>

**P867** 			<RmtInf>

**P868** 				<Ustrd>LIFE INSURANCE PAYMENT/ JULY 2012</Ustrd>

**P869** 			</RmtInf>

**P870** 		</DrctDbtTxInf>

**P871** 		<DrctDbtTxInf>

**P872** 			<PmtId>

**P873** 				<EndToEndId>AY090327/456</EndToEndId>

**P874** 			</PmtId>

**P875** 			<PmtTpInf>

**P876** 				<InstrPrty>NORM</InstrPrty>

**P877** 				<SvcLvl>

**P878** 					<Prtry>VERPA-1</Prtry>

**P879** 				</SvcLvl>

**P880** 				<SeqTp>OOFF</SeqTp>

**P881** 			</PmtTpInf>

**P882** 			<InstdAmt Ccy="USD">985</InstdAmt>

**P883** 			<ChrgBr>SHAR</ChrgBr>

**P884** 			<DrctDbtTx>

**P885** 				<PreNtfctnId>VIRGAY2435/2012</PreNtfctnId>

**P886** 				<PreNtfctnDt>2012-06-08</PreNtfctnDt>

**P887** 			</DrctDbtTx>

**P888** 			<DbtrAgt>

**P889** 				<FinInstnId>

**P890** 					<BICFI>CCCCUS27</BICFI>

**P891** 				</FinInstnId>

**P892** 			</DbtrAgt>

**P893** 			<Dbtr>

**P894** 				<Nm>Lee</Nm>

**P895** 				<PstlAdr>

**P896** 					<StrtNm>Cross Road</StrtNm>

**P897** 					<BldgNb>45</BldgNb>

**P898** 					<PstCd>NJ07399</PstCd>

**P899** 					<TwnNm>Jersey City</TwnNm>

**P900** 					<Ctry>US</Ctry>

**P901** 				</PstlAdr>

**P902** 			</Dbtr>

**P903** 			<DbtrAcct>

**P904** 				<Id>

**P905** 					<Othr>

**P906** 						<Id>789101</Id>

**P907** 					</Othr>

**P908** 				</Id>

**P909** 			</DbtrAcct>

**P910** 			<RmtInf>

**P911** 				<Ustrd>CAR INSURANCE PREMIUM</Ustrd>

**P912** 			</RmtInf>

**P913** 		</DrctDbtTxInf>

**P914** 	</PmtInf>

**P915** </CstmrDrctDbtInitn>

