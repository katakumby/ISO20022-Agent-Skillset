---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["Business Examples", "Securities Account Query - reda.019.001.01"]
content_origin: "source-transcription"
---

# Securities Account Query - reda.019.001.01

Source: [src-000371](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path Business Examples / Securities Account Query - reda.019.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P496** Securities Account Query - reda.019.001.01

**P497** Description

**P498** The Securities Account Query message can be used to perform the following queries:

**P499** Securities Account Reference Data Query;

**P500** Securities Account List Query.

**P501** In this example the Party CSDAXXYYAAA perform a Securities Account List Query to request a list of securities account.

**P502** Message Instance

**P503** <Document>

**P504** 	<SctiesAcctQry>

**P505** 		<MsgHdr>

**P506** 			<MsgId>SAMPLESALIQUERY</MsgId>

**P507** 			<ReqTp>

**P508** 				<Prtry>

**P509** 					<Id>SALI</Id>

**P510** 					<SchmeNm>SACQ</SchmeNm>

**P511** 					<Issr>T2S</Issr>

**P512** 				</Prtry>

**P513** 			</ReqTp>

**P514** 		</MsgHdr>

**P515** 		<SchCrit>

**P516** 			<AcctSvcr>

**P517** 				<Id>

**P518** 					<AnyBIC>CSDAXXYYAAA</AnyBIC>

**P519** 				</Id>

**P520** 			</AcctSvcr>

**P521** 		</SchCrit>

**P522** 	</SctiesAcctQry>

**P523** </Document>

