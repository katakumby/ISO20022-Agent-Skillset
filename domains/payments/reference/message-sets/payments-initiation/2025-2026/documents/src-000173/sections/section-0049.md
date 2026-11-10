---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "CustomerPaymentReversal pain.007.001.13"]
content_origin: "source-transcription"
---

# CustomerPaymentReversal pain.007.001.13

Source: [src-000173](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx). Locator: heading path Business Examples / CustomerPaymentReversal pain.007.001.13.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P664** CustomerPaymentReversal pain.007.001.13

**P665** Description	

**P666** On 17 June 2012, date of the collection from debtor Schneider, Ritcom electricity company realises that the direct debit instruction sent on 9 June 2012 was a duplicated instruction. As settlement of the direct debit already took place, Ritcom electricity company initiates a CustomerPaymentReversal message and sends it to its account servicer AAAADEFF. Any potential charges relating to this reversal payment, paid by Schneider, will be deducted from the next invoice.

**P667** Business Data

**P668** CustomerPaymentReversal from Ritcom to AAAADEFF :

[T27 - complete table](../tables/tbl-0027.md)

**P669** Message Instance

**P670** <CstmrPmtRvsl>

**P671** 	<GrpHdr>

**P672** 		<MsgId>RIT-REV-20120617-456f</MsgId>

**P673** 		<CreDtTm>2012-06-17T15:38:00</CreDtTm>

**P674** 		<NbOfTxs>1</NbOfTxs>

**P675** 		<InitgPty>

**P676** 			<Nm>Ritcom</Nm>

**P677** 			<PstlAdr>

**P678** 				<StrtNm>Schueman Strasse</StrtNm>

**P679** 				<BldgNb>18</BldgNb>

**P680** 				<PstCd>60017</PstCd>

**P681** 				<TwnNm>Frankfurt am Main</TwnNm>

**P682** 				<Ctry>DE</Ctry>

**P683** 			</PstlAdr>

**P684** 		</InitgPty>

**P685** 		<DbtrAgt>

**P686** 			<FinInstnId>

**P687** 				<BICFI>BBBBDE33</BICFI>

**P688** 			</FinInstnId>

**P689** 		</DbtrAgt>

**P690** 		<CdtrAgt>

**P691** 			<FinInstnId>

**P692** 				<BICFI>AAAADEFF</BICFI>

**P693** 			</FinInstnId>

**P694** 		</CdtrAgt>

**P695** 	</GrpHdr>

**P696** 	<OrgnlGrpInf>

**P697** 		<OrgnlMsgId>RITCOM1234</OrgnlMsgId>

**P698** 		<OrgnlMsgNmId>pain.008.001.12</OrgnlMsgNmId>

**P699** 		<OrgnlCreDtTm>2012-06-09T09:18:00</OrgnlCreDtTm>

**P700** 	</OrgnlGrpInf>

**P701** 	<OrgnlPmtInfAndRvsl>

**P702** 		<OrgnlPmtInfId>RIT/0053</OrgnlPmtInfId>

**P703** 		<TxInf>

**P704** 			<RvslId>RIT5467</RvslId>

**P705** 			<OrgnlEndToEndId>RIT/012010-2562C26</OrgnlEndToEndId>

**P706** 			<OrgnlInstdAmt Ccy="EUR">286</OrgnlInstdAmt>

**P707** 			<RvsdInstdAmt Ccy="EUR">286</RvsdInstdAmt>

**P708** 			<RvslRsnInf>

**P709** 				<Orgtr>

**P710** 					<Nm>Ritcom</Nm>

**P711** 					<PstlAdr>

**P712** 						<StrtNm>Schueman Strasse</StrtNm>

**P713** 						<BldgNb>18</BldgNb>

**P714** 						<PstCd>60017</PstCd>

**P715** 						<TwnNm>Frankfurt am Main</TwnNm>

**P716** 						<Ctry>DE</Ctry>

**P717** 					</PstlAdr>

**P718** 				</Orgtr>

**P719** 				<Rsn>

**P720** 					<Cd>AM05</Cd>

**P721** 				</Rsn>

**P722** 			</RvslRsnInf>

**P723** 			<OrgnlTxRef>

**P724** 				<ReqdColltnDt>2010-06-16</ReqdColltnDt>

**P725** 				<MndtRltdInf>

**P726** 					<DrctDbtMndt>

**P727** 						<MndtId>RIT04/av002</MndtId>

**P728** 					</DrctDbtMndt>

**P729** 				</MndtRltdInf>

**P730** 				<Dbtr>

**P731** 					<Pty>

**P732** 						<Nm>Schneider</Nm>

**P733** 						<PstlAdr>

**P734** 							<StrtNm>Kuertman Strasse</StrtNm>

**P735** 							<BldgNb>45</BldgNb>

**P736** 							<PstCd>50475</PstCd>

**P737** 							<TwnNm>Koln</TwnNm>

**P738** 							<Ctry>DE</Ctry>

**P739** 						</PstlAdr>

**P740** 					</Pty>

**P741** 				</Dbtr>

**P742** 				<DbtrAcct>

**P743** 					<Id>

**P744** 						<IBAN>DE89370400440332014000</IBAN>

**P745** 					</Id>

**P746** 				</DbtrAcct>

**P747** 				<Cdtr>

**P748** 					<Pty>

**P749** 						<Nm>Ritcom</Nm>

**P750** 						<PstlAdr>

**P751** 							<StrtNm>Schueman Strasse</StrtNm>

**P752** 							<BldgNb>18</BldgNb>

**P753** 							<PstCd>60017</PstCd>

**P754** 							<TwnNm>Frankfurt am Main</TwnNm>

**P755** 							<Ctry>DE</Ctry>

**P756** 						</PstlAdr>

**P757** 					</Pty>

**P758** 				</Cdtr>

**P759** 			</OrgnlTxRef>

**P760** 		</TxInf>

**P761** 	</OrgnlPmtInfAndRvsl>

**P762** </CstmrPmtRvsl>

