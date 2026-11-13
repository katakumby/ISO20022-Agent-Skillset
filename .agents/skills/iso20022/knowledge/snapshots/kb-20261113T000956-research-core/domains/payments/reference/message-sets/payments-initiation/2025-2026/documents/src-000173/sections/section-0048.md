---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "CustomerPaymentStatusReport pain.002.001.15 - 2"]
content_origin: "source-transcription"
---

# CustomerPaymentStatusReport pain.002.001.15 - 2

Source: [src-000173](../../../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Locator: heading path Business Examples / CustomerPaymentStatusReport pain.002.001.15 - 2.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P577** CustomerPaymentStatusReport pain.002.001.15 - 2

**P578** Description

**P579** AAAAUS29 received an FIToFIPaymentStatusReport from its correspondent, ABABUS23, containing reject information about a previously sent FIToFICustomerDirectDebit. As AAAAUS29 has not yet credited the account of the original initiating party (Virgay) of the direct debit, AAAAUS29 in its turn informs Virgay about the rejection of the CustomerDirectDebitInitiation sent on 28 June 2012.

**P580** Business Description

**P581** CustomerPaymentStatusReport from AAAAUS29 to Virgay:

[T26 - complete table](../tables/tbl-0026.md)

**P582** Message Instance

**P583** <CstmrPmtStsRpt>

**P584** 	<GrpHdr>

**P585** 		<MsgId>AAAAUS29_5678c</MsgId>

**P586** 		<CreDtTm>2012-06-29T15:49:00</CreDtTm>

**P587** 		<InitgPty>

**P588** 			<Nm>Virgay</Nm>

**P589** 			<PstlAdr>

**P590** 				<StrtNm>Virginia Lane</StrtNm>

**P591** 				<BldgNb>36</BldgNb>

**P592** 				<PstCd>NJ 07311</PstCd>

**P593** 				<TwnNm>Jersey City</TwnNm>

**P594** 				<Ctry>US</Ctry>

**P595** 			</PstlAdr>

**P596** 		</InitgPty>

**P597** 		<CdtrAgt>

**P598** 			<FinInstnId>

**P599** 				<BICFI>AAAAUS29</BICFI>

**P600** 			</FinInstnId>

**P601** 		</CdtrAgt>

**P602** 	</GrpHdr>

**P603** 	<OrgnlGrpInfAndSts>

**P604** 		<OrgnlMsgId>CAVAY1234</OrgnlMsgId>

**P605** 		<OrgnlMsgNmId>pain.008.001.12</OrgnlMsgNmId>

**P606** 		<OrgnlCreDtTm>2012-06-28T14:25:00</OrgnlCreDtTm>

**P607** 	</OrgnlGrpInfAndSts>

**P608** 	<OrgnlPmtInfAndSts>

**P609** 		<OrgnlPmtInfId>JKL_774</OrgnlPmtInfId>

**P610** 		<TxInfAndSts>

**P611** 			<StsId>RIT2012 657B</StsId>

**P612** 			<OrgnlEndToEndId>VA100327/0123</OrgnlEndToEndId>

**P613** 			<TxSts>RJCT</TxSts>

**P614** 			<StsRsnInf>

**P615** 				<Orgtr>

**P616** 					<Id>

**P617** 						<OrgId>

**P618** 							<AnyBIC>ABABUS23</AnyBIC>

**P619** 						</OrgId>

**P620** 					</Id>

**P621** 				</Orgtr>

**P622** 				<Rsn>

**P623** 					<Cd>AM05</Cd>

**P624** 				</Rsn>

**P625** 			</StsRsnInf>

**P626** 			<OrgnlTxRef>

**P627** 				<Amt>

**P628** 					<InstdAmt Ccy="USD">1025</InstdAmt>

**P629** 				</Amt>

**P630** 				<ReqdColltnDt>2012-07-02</ReqdColltnDt>

**P631** 				<MndtRltdInf>

**P632** 					<DrctDbtMndt>

**P633** 						<MndtId>VIRGAY123</MndtId>

**P634** 					</DrctDbtMndt>

**P635** 				</MndtRltdInf>

**P636** 				<Dbtr>

**P637** 					<Pty>

**P638** 						<Nm>Jones</Nm>

**P639** 						<PstlAdr>

**P640** 							<StrtNm>Hudson Street</StrtNm>

**P641** 							<BldgNb>19</BldgNb>

**P642** 							<PstCd>NJ 07302</PstCd>

**P643** 							<TwnNm>Jersey City</TwnNm>

**P644** 							<Ctry>US</Ctry>

**P645** 						</PstlAdr>

**P646** 					</Pty>

**P647** 				</Dbtr>

**P648** 				<Cdtr>

**P649** 					<Pty>

**P650** 						<Nm>Virgay</Nm>

**P651** 						<PstlAdr>

**P652** 							<StrtNm>Virginia Lane</StrtNm>

**P653** 							<BldgNb>36</BldgNb>

**P654** 							<PstCd>NJ 07311</PstCd>

**P655** 							<TwnNm>Jersey City</TwnNm>

**P656** 							<Ctry>US</Ctry>

**P657** 						</PstlAdr>

**P658** 					</Pty>

**P659** 				</Cdtr>

**P660** 			</OrgnlTxRef>

**P661** 		</TxInfAndSts>

**P662** 	</OrgnlPmtInfAndSts>

**P663** </CstmrPmtStsRpt>

