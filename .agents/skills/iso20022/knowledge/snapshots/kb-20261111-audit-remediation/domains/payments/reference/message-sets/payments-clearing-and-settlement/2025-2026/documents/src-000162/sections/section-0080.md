---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FIToFICustomerDirectDebit pacs.003.001.12"]
content_origin: "source-transcription"
---

# FIToFICustomerDirectDebit pacs.003.001.12

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path Business Examples / FIToFICustomerDirectDebit pacs.003.001.12.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P732** FIToFICustomerDirectDebit pacs.003.001.12

**P733** Description

**P734** On 28 June 2015, following the receipt of a CustomerDirectDebitInitiation message from its customer Virgay, AAAAUS29 in its turn sends an FIToFICustomerDirectDebit message to ABABUS23, the common correspondent for AAAAUS29 and BBBBUS39, the agent of debtor Jones.

**P735** AAAAUS29 instructs ABABUS23, under Service Level CTRV - 356, to collect USD 1025 from account 123456, owned by Jones, the debtor, and serviced by BBBBUS39. The mandate related information is also provided: the mandate reference is VIRGAY123 and the mandate was signed by Jones on 13 July 2008. The last collection is due to take place on 13 July 2015. The payment is for life insurance. The requested collection date is 13 July 20102 and charges related to the handling of the instruction are shared between the creditor and the debtor.

**P736** The CustomerDirectDebitInitiation instruction sent by Virgay to AAAAUS29 is documented in the business example section of the CustomerDirectDebitInitiation message in the Payments Initiation Message Reference Guide.

**P737** Business Data

**P738** FIToFICustomerDirectDebit from AAAAUS29 to ABABUS23:

[T29 - complete table](../tables/tbl-0029.md)

**P739** Message Instance

**P740** <FIToFICstmrDrctDbt>

**P741** 	<GrpHdr>

**P742** 		<MsgId>AAAA100628-123v</MsgId>

**P743** 		<CreDtTm>2015-06-28T10:05:00</CreDtTm>

**P744** 			<NbOfTxs>1</NbOfTxs>

**P745** 		<IntrBkSttlmDt>2015-06-28</IntrBkSttlmDt>

**P746** 		<SttlmInf>

**P747** 			<SttlmMtd>INDA</SttlmMtd>

**P748** 		</SttlmInf>

**P749** 		<PmtTpInf>

**P750** 			<InstrPrty>NORM</InstrPrty>

**P751** 			<SvcLvl>

**P752** 				<Prtry>CTRV-356</Prtry>

**P753** 			</SvcLvl>

**P754** 			<SeqTp>RCUR</SeqTp>

**P755** 		</PmtTpInf>

**P756** 		<InstgAgt>

**P757** 			<FinInstnId>

**P758** 				<BICFI>AAAAUS29</BICFI>

**P759** 			</FinInstnId>

**P760** 		</InstgAgt>

**P761** 		<InstdAgt>

**P762** 			<FinInstnId>

**P763** 				<BICFI>ABABUS23</BICFI>

**P764** 			</FinInstnId>

**P765** 		</InstdAgt>

**P766** 	</GrpHdr>

**P767** 	<DrctDbtTxInf>

**P768** 		<PmtId>

**P769** 			<EndToEndId>VA060713/0123</EndToEndId>

**P770** 			<TxId>AAAAUS29/100628/ad458</TxId>

**P771** 		</PmtId>

**P772** 		<IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>

**P773** 		<InstdAmt Ccy="USD">1025</InstdAmt>

**P774** 		<ChrgBr>SHAR</ChrgBr>

**P775** 		<ReqdColltnDt>2015-07-13</ReqdColltnDt>

**P776** 		<DrctDbtTx>

**P777** 			<MndtRltdInf>

**P778** 				<MndtId>VIRGAY123</MndtId>

**P779** 				<DtOfSgntr>2008-07-13</DtOfSgntr>

**P780** 				<FnlColltnDt>2015-07-13</FnlColltnDt>

**P781** 				<Frqcy><Tp>YEAR</Tp></Frqcy>

**P782** 			</MndtRltdInf>

**P783** 		</DrctDbtTx>

**P784** 		<Cdtr>

**P785** 			<Nm>Virgay</Nm>

**P786** 			<PstlAdr>

**P787** 				<StrtNm>Virginia Lane</StrtNm>

**P788** 					<BldgNb>36</BldgNb>

**P789** 				<PstCd>NJ 07311</PstCd>

**P790** 				<TwnNm>Jersey City</TwnNm>

**P791** 				<Ctry>US</Ctry>

**P792** 			</PstlAdr>

**P793** 		</Cdtr>

**P794** 		<CdtrAcct>

**P795** 			<Id>

**P796** 				<Othr>

**P797** 					<Id>789123</Id>

**P798** 				</Othr>

**P799** 			</Id>

**P800** 		</CdtrAcct>

**P801** 		<CdtrAgt>

**P802** 			<FinInstnId>

**P803** 				<BICFI>AAAAUS29</BICFI>

**P804** 			</FinInstnId>

**P805** 		</CdtrAgt>

**P806** 		<Dbtr>

**P807** 			<Nm>Jones</Nm>

**P808** 			<PstlAdr>

**P809** 				<StrtNm>Hudson Street</StrtNm>

**P810** 				<BldgNb>19</BldgNb>

**P811** 				<PstCd>NJ 07302</PstCd>

**P812** 				<TwnNm>Jersey City</TwnNm>

**P813** 				<Ctry>US</Ctry>

**P814** 			</PstlAdr>

**P815** 		</Dbtr>

**P816** 			<DbtrAcct>

**P817** 			<Id>

**P818** 				<Othr>

**P819** 					<Id>123456</Id>

**P820** 				</Othr>

**P821** 			</Id>

**P822** 		</DbtrAcct>

**P823** 		<DbtrAgt>

**P824** 			<FinInstnId>

**P825** 				<BICFI>BBBBUS39</BICFI>

**P826** 			</FinInstnId>

**P827** 		</DbtrAgt>

**P828** 		<Purp>

**P829** 			<Cd>LIFI</Cd>

**P830** 		</Purp>

**P831** 		<RmtInf>

**P832** 			<Ustrd>LIFE INSURANCE PAYMENT/JULY 2015</Ustrd>

**P833** 		</RmtInf>

**P834** 	</DrctDbtTxInf>

**P835** </FIToFICstmrDrctDbt>

