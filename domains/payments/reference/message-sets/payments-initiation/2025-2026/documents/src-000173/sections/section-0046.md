---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "CustomerCreditTransferInitiation pain.001.001.13"]
content_origin: "source-transcription"
---

# CustomerCreditTransferInitiation pain.001.001.13

Source: [src-000173](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart1_PaymentsInitiation_2025_2026_v2.docx). Locator: heading path Business Examples / CustomerCreditTransferInitiation pain.001.001.13.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P320** CustomerCreditTransferInitiation pain.001.001.13

**P321** Description

**P322** ABC Corporation, New York has received three invoices:

**P323** Invoice 1

**P324** An invoice with number 4562, dated 08 September 2012 from DEF Electronics, London: 10 million JPY needs to be paid to DEF Electronics account 23683707994215 with AAAA Bank, London (AAAAGB2L). ABC Corporation assigns reference ABC/4562/2012-09-08 to the payment. Payment transaction charges are shared between ABC Corporation and DEF Electronics.

**P325** Invoice 2

**P326** An invoice with number ABC-13679, dated 15 September 2012 from GHI Semiconductors, Brussels: 500,000 EUR needs to be paid to GHI Semiconductors account BE30001216371411 with DDDD Bank, Belgium (DDDDBEBB). ABC Corporation assigns reference ABC/ABC-13679/2012-09-15 to the payment. The accounts receivable department of GHI Semiconductors needs to be advised when the funds have been credited on the account on telephone number +32/2/2222222. GHI Semiconductors will bear all payment transaction charges.

**P327** Invoice 3

**P328** An invoice with number 987-AC, dated 27 September 2012, from their branch ABC Corporation, California: 1 million USD needs to be paid to the branch account 4895623 with BBBB Bank, San Francisco (BBBBUS66). ABC assigns a reference ABC/987-AC/2012-09-27 to the payment. Payment transaction charges are shared.

**P329** ABC Corporation holds an account 00125574999 with BBBB Bank, New York (BBBBUS33) and instructs its bank to execute payment of the invoices with a CustomerCreditTransferInitiation message.

**P330** Business Data

**P331** CustomerCreditTransferInitiation from ABC Corporation, New York to BBBB Bank, New York:

[T24 - complete table](../tables/tbl-0024.md)

**P332** Message Instance

**P333** <CstmrCdtTrfInitn>

**P334** 	<GrpHdr>

**P335** 		<MsgId>ABC/120928/CCT001</MsgId>

**P336** 		<CreDtTm>2012-09-28T14:07:00</CreDtTm>

**P337** 		<NbOfTxs>3</NbOfTxs>

**P338** 		<CtrlSum>11500000</CtrlSum>

**P339** 		<InitgPty>

**P340** 			<Nm>ABC Corporation</Nm>

**P341** 			<PstlAdr>

**P342** 				<StrtNm>Times Square</StrtNm>

**P343** 				<BldgNb>7</BldgNb>

**P344** 				<PstCd>NY 10036</PstCd>

**P345** 				<TwnNm>New York</TwnNm>

**P346** 				<Ctry>US</Ctry>

**P347** 			</PstlAdr>

**P348** 		</InitgPty>

**P349** 	</GrpHdr>

**P350** 	<PmtInf>

**P351** 		<PmtInfId>ABC/086</PmtInfId>

**P352** 		<PmtMtd>TRF</PmtMtd>

**P353** 		<BtchBookg>false</BtchBookg>

**P354** 		<ReqdExctnDt>

**P355** 			<Dt>2012-09-29</Dt>

**P356** 		</ReqdExctnDt>

**P357** 		<Dbtr>

**P358** 			<Nm>ABC Corporation</Nm>

**P359** 			<PstlAdr>

**P360** 				<StrtNm>Times Square</StrtNm>

**P361** 				<BldgNb>7</BldgNb>

**P362** 				<PstCd>NY 10036</PstCd>

**P363** 				<TwnNm>New York</TwnNm>

**P364** 				<Ctry>US</Ctry>

**P365** 			</PstlAdr>

**P366** 		</Dbtr>

**P367** 		<DbtrAcct>

**P368** 			<Id>

**P369** 				<Othr>

**P370** 					<Id>00125574999</Id>

**P371** 				</Othr>

**P372** 			</Id>

**P373** 		</DbtrAcct>

**P374** 		<DbtrAgt>

**P375** 			<FinInstnId>

**P376** 				<BICFI>BBBBUS33</BICFI>

**P377** 			</FinInstnId>

**P378** 		</DbtrAgt>

**P379** 		<CdtTrfTxInf>

**P380** 			<PmtId>

**P381** 				<InstrId>ABC/120928/CCT001/01</InstrId>

**P382** 				<EndToEndId>ABC/4562/2012-09-08</EndToEndId>

**P383** 			</PmtId>

**P384** 			<Amt>

**P385** 				<InstdAmt Ccy="JPY">10000000</InstdAmt>

**P386** 			</Amt>

**P387** 			<ChrgBr>SHAR</ChrgBr>

**P388** 			<CdtrAgt>

**P389** 				<FinInstnId>

**P390** 					<BICFI>AAAAGB2L</BICFI>

**P391** 				</FinInstnId>

**P392** 			</CdtrAgt>

**P393** 			<Cdtr>

**P394** 				<Nm>DEF Electronics</Nm>

**P395** 				<PstlAdr>

**P396** 					<AdrLine>Corn Exchange 5th Floor</AdrLine>

**P397** 					<AdrLine>Mark Lane 55</AdrLine>

**P398** 					<AdrLine>EC3R7NE London</AdrLine>

**P399** 					<AdrLine>GB</AdrLine>

**P400** 				</PstlAdr>

**P401** 			</Cdtr>

**P402** 			<CdtrAcct>

**P403** 				<Id>

**P404** 					<Othr>

**P405** 						<Id>23683707994125</Id>

**P406** 					</Othr>

**P407** 				</Id>

**P408** 			</CdtrAcct>

**P409** 			<Purp>

**P410** 				<Cd>GDDS</Cd>

**P411** 			</Purp>

**P412** 			<RmtInf>

**P413** 				<Strd>

**P414** 					<RfrdDocInf>

**P415** 						<Tp>

**P416** 							<CdOrPrtry>

**P417** 								<Cd>CINV</Cd>

**P418** 							</CdOrPrtry>

**P419** 						</Tp>

**P420** 						<Nb>4562</Nb>

**P421** 						<RltdDt>

**P422** 						<Tp>

**P423** 							<Cd>INDA</Cd>

**P424** 						</Tp>

**P425** 						<Dt>2012-09-08</Dt>									

**P426** 						</RltdDt>							

**P427** 					</RfrdDocInf>

**P428** 				</Strd>

**P429** 			</RmtInf>

**P430** 		</CdtTrfTxInf>

**P431** 		<CdtTrfTxInf>

**P432** 			<PmtId>

**P433** 				<InstrId>ABC/120928/CCT001/2</InstrId>

**P434** 				<EndToEndId>ABC/ABC-13679/2012-09-15</EndToEndId>

**P435** 			</PmtId>

**P436** 			<Amt>

**P437** 				<InstdAmt Ccy="EUR">500000</InstdAmt>

**P438** 			</Amt>

**P439** 			<ChrgBr>CRED</ChrgBr>

**P440** 			<CdtrAgt>

**P441** 				<FinInstnId>

**P442** 					<BICFI>DDDDBEBB</BICFI>

**P443** 				</FinInstnId>

**P444** 			</CdtrAgt>

**P445** 			<Cdtr>

**P446** 				<Nm>GHI Semiconductors</Nm>

**P447** 				<PstlAdr>

**P448** 					<StrtNm>Avenue Brugmann</StrtNm>

**P449** 					<BldgNb>415</BldgNb>

**P450** 					<PstCd>1180</PstCd>

**P451** 					<TwnNm>Brussels</TwnNm>

**P452** 					<Ctry>BE</Ctry>

**P453** 				</PstlAdr>

**P454** 			</Cdtr>

**P455** 			<CdtrAcct>

**P456** 				<Id>

**P457** 					<IBAN>BE30001216371411</IBAN>

**P458** 				</Id>

**P459** 			</CdtrAcct>

**P460** 			<InstrForCdtrAgt>

**P461** 				<Cd>PHOB</Cd>

**P462** 				<InstrInf>+32/2/2222222</InstrInf>

**P463** 			</InstrForCdtrAgt>

**P464** 			<Purp>

**P465** 				<Cd>GDDS</Cd>

**P466** 			</Purp>

**P467** 			<RmtInf>

**P468** 				<Strd>

**P469** 					<RfrdDocInf>

**P470** 						<Tp>

**P471** 							<CdOrPrtry>

**P472** 								<Cd>CINV</Cd>

**P473** 							</CdOrPrtry>

**P474** 						</Tp>

**P475** 						<Nb>ABC-13679</Nb>

**P476** 						<RltdDt>

**P477** 						<Tp>

**P478** 							<Cd>INDA</Cd>

**P479** 						</Tp>

**P480** 						<Dt>2012-09-15</Dt>									

**P481** 						</RltdDt>						

**P482** 					</RfrdDocInf>

**P483** 				</Strd>

**P484** 			</RmtInf>

**P485** 		</CdtTrfTxInf>

**P486** 		<CdtTrfTxInf>

**P487** 			<PmtId>

**P488** 				<InstrId>ABC/120928/CCT001/3</InstrId>

**P489** 				<EndToEndId>ABC/987-AC/2012-09-27</EndToEndId>

**P490** 			</PmtId>

**P491** 			<Amt>

**P492** 				<InstdAmt Ccy="USD">1000000</InstdAmt>

**P493** 			</Amt>

**P494** 			<ChrgBr>SHAR</ChrgBr>

**P495** 			<CdtrAgt>

**P496** 				<FinInstnId>

**P497** 					<BICFI>BBBBUS66</BICFI>

**P498** 				</FinInstnId>

**P499** 			</CdtrAgt>

**P500** 			<Cdtr>

**P501** 				<Nm>ABC Corporation</Nm>

**P502** 				<PstlAdr>

**P503** 					<Dept>Treasury department</Dept>

**P504** 					<StrtNm>Bush Street</StrtNm>

**P505** 					<BldgNb>13</BldgNb>

**P506** 					<PstCd>CA 94108</PstCd>

**P507** 					<TwnNm>San Francisco</TwnNm>

**P508** 					<Ctry>US</Ctry>

**P509** 				</PstlAdr>

**P510** 			</Cdtr>

**P511** 			<CdtrAcct>

**P512** 				<Id>

**P513** 					<Othr>

**P514** 						<Id>4895623</Id>

**P515** 					</Othr>

**P516** 				</Id>

**P517** 			</CdtrAcct>

**P518** 			<Purp>

**P519** 				<Cd>INTC</Cd>

**P520** 			</Purp>

**P521** 			<RmtInf>

**P522** 				<Strd>

**P523** 					<RfrdDocInf>

**P524** 						<Tp>

**P525** 							<CdOrPrtry>

**P526** 								<Cd>CINV</Cd>

**P527** 							</CdOrPrtry>

**P528** 						</Tp>

**P529** 						<Nb>987-AC</Nb>

**P530** 						<RltdDt>

**P531** 						<Tp>

**P532** 							<Cd>INDA</Cd>

**P533** 						</Tp>

**P534** 						<Dt>2012-09-27</Dt>									

**P535** 						</RltdDt>						

**P536** 					</RfrdDocInf>

**P537** 				</Strd>

**P538** 			</RmtInf>

**P539** 		</CdtTrfTxInf>

**P540** 	</PmtInf>

**P541** </CstmrCdtTrfInitn>

