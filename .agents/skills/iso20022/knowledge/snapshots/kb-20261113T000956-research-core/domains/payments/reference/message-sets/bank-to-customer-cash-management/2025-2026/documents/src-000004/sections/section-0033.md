---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "AccountReportingRequest camt.060.001.07"]
content_origin: "source-transcription"
---

# AccountReportingRequest camt.060.001.07

Source: [src-000004](../../../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md). Locator: heading path Business Examples / AccountReportingRequest camt.060.001.07.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P515** AccountReportingRequest camt.060.001.07

**P516** Description

**P517** On 27 October 2015, AAAABEBB sends an AccountReportingRequest message to its account servicer BBBBUS33 to request a BankToCustomerStatement for that day.

**P518** Business Data

[T21 - complete table](../tables/tbl-0021.md)

**P519** Message Instance

**P520** <AcctRptgReq>

**P521** 	<GrpHdr>

**P522** 		<MsgId>EXAMPLE camt.060</MsgId>

**P523** 		<CreDtTm>2015-10-27T17:15:00</CreDtTm>

**P524** 	</GrpHdr>

**P525** 	<RptgReq>

**P526** 		<ReqdMsgNmId>camt.052.001.08</ReqdMsgNmId>

**P527** 		<Acct>

**P528** 			<Id>

**P529** 				<Othr>

**P530** 					<Id>310141014141</Id>

**P531** 				</Othr>

**P532** 			</Id>

**P533** 		</Acct>

**P534** 		<AcctOwnr>

**P535** 			<Agt>

**P536** 				<FinInstnId>

**P537** 					<BICFI>AAAABEBB</BICFI>

**P538** 				</FinInstnId>

**P539** 			</Agt>

**P540** 		</AcctOwnr>

**P541** 		<RptgPrd>

**P542** 			<FrToDt>

**P543** 				<FrDt>2015-10-27</FrDt>

**P544** 			</FrToDt>

**P545** 			<FrToTm>

**P546** 				<FrTm>07:30:00</FrTm>

**P547** 			</FrToTm>

**P548** 			<Tp>ALLL</Tp>

**P549** 		</RptgPrd>

**P550** 	</RptgReq>

**P551** </AcctRptgReq>

