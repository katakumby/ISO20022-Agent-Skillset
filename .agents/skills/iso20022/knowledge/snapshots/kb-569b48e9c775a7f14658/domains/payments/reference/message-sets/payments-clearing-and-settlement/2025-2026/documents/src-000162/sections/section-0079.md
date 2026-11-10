---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FIToFIPaymentStatusReport  pacs.002.001.16"]
content_origin: "source-transcription"
---

# FIToFIPaymentStatusReport  pacs.002.001.16

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path Business Examples / FIToFIPaymentStatusReport  pacs.002.001.16.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P650** FIToFIPaymentStatusReport  pacs.002.001.16

**P651** Description

**P652** On 28 June 2015, ABABUS23 received a FIToFICustomerDirectDebit message from AAAAUS29. On 29 June 2015, ABABUS23 rejects the FIToFICustomerDirectDebit message by sending a FIToFIPaymentStatusReport message to AAAAUS29, referring to the original instruction and indicating the reason for the rejection.

**P653** Related Message Examples

**P654** The FIToFICustomerDirectDebit instruction from AAAAUS29 to ABABUS23 is included in the business example section of the FIToFICustomerDirectDebit message.

**P655** As AAAUS29 has not yet credited the account of its customer, Virgay, in turn, AAAAUS29 will send a CustomerPaymentStatusReport to inform Virgay of the rejection. This example is included in the business example section of the PaymentStatusReport message in the Payments Initiation Message Reference Guide.

**P656** Business Data

**P657** PaymentStatusReport from ABABUS23 to AAAAUS29:

[T28 - complete table](../tables/tbl-0028.md)

**P658** Message Instance

**P659** <FIToFIPmtStsRpt>

**P660** 	<GrpHdr>

**P661** 		<MsgId>ABABUS23-STATUS-456/04</MsgId>

**P662** 		<CreDtTm>2015-06-29T09:56:00</CreDtTm>

**P663** 		<InstgAgt>

**P664** 			<FinInstnId>

**P665** 				<BICFI>ABABUS23</BICFI>

**P666** 			</FinInstnId>

**P667** 		</InstgAgt>

**P668** 		<InstdAgt>

**P669** 			<FinInstnId>

**P670** 				<BICFI>AAAAUS29</BICFI>

**P671** 			</FinInstnId>

**P672** 		</InstdAgt>

**P673** 	</GrpHdr>

**P674** 	<OrgnlGrpInfAndSts>

**P675** 		<OrgnlMsgId>AAAA100628-123v</OrgnlMsgId>

**P676** 		<OrgnlMsgNmId>pacs.003.001.12</OrgnlMsgNmId>

**P677** 		<OrgnlCreDtTm>2015-06-28T10:05:00</OrgnlCreDtTm>

**P678** 	</OrgnlGrpInfAndSts>

**P679** 	<TxInfAndSts>

**P680** 		<StsId>AB/8568</StsId>

**P681** 		<OrgnlEndToEndId>VA060327/0123</OrgnlEndToEndId>

**P682** 		<OrgnlTxId>AAAAUS29/100628/ad458</OrgnlTxId>

**P683** 		<TxSts>RJCT</TxSts>

**P684** 		<StsRsnInf>

**P685** 			<Orgtr>

**P686** 				<Id>

**P687** 					<OrgId>

**P688** 						<AnyBIC>ABABUS23</AnyBIC>

**P689** 					</OrgId>

**P690** 				</Id>

**P691** 			</Orgtr>

**P692** 			<Rsn>

**P693** 				<Cd>AM05</Cd>

**P694** 			</Rsn>

**P695** 		</StsRsnInf>

**P696** 		<OrgnlTxRef>

**P697** 			<IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>

**P698** 			<IntrBkSttlmDt>2015-06-28</IntrBkSttlmDt>

**P699** 			<ReqdColltnDt>2015-07-13</ReqdColltnDt>

**P700** 			<MndtRltdInf>

**P701** 				<DrctDbtMndt>

**P702** 					<MndtId>VIRGAY123</MndtId>

**P703** 				</DrctDbtMndt>

**P704** 			</MndtRltdInf>

**P705** 			<Dbtr>

**P706** 				<Pty>

**P707** 					<Nm>Jones</Nm>

**P708** 					<PstlAdr>

**P709** 						<StrtNm>Hudson Street</StrtNm>

**P710** 						<BldgNb>19</BldgNb>

**P711** 						<PstCd>NJ 07302</PstCd>

**P712** 						<TwnNm>Jersey City</TwnNm>

**P713** 						<Ctry>US</Ctry>

**P714** 					</PstlAdr>

**P715** 				</Pty>	

**P716** 			</Dbtr>

**P717** 			<Cdtr>

**P718** 				<Pty>

**P719** 					<Nm>Virgay</Nm>

**P720** 					<PstlAdr>

**P721** 						<StrtNm>Virginia Lane</StrtNm>

**P722** 						<BldgNb>36</BldgNb>

**P723** 						<PstCd>NJ 07311</PstCd>

**P724** 						<TwnNm>Jersey City</TwnNm>

**P725** 						<Ctry>US</Ctry>

**P726** 					</PstlAdr>

**P727** 				</Pty>

**P728** 			</Cdtr>

**P729** 		</OrgnlTxRef>

**P730** 	</TxInfAndSts>

**P731** </FIToFIPmtStsRpt>

