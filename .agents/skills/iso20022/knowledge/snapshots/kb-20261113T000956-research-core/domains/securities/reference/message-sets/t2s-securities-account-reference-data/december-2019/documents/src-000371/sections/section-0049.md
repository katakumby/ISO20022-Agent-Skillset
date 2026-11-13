---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["Business Examples", "Securities Account Modification Request - reda.023.001.01"]
content_origin: "source-transcription"
---

# Securities Account Modification Request - reda.023.001.01

Source: [src-000371](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path Business Examples / Securities Account Modification Request - reda.023.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P373** Securities Account Modification Request - reda.023.001.01

**P374** Description

**P375** In this example, the instructing party wants to update the negative position flag of the securities account SECACCCSDPXXYYAAA.

**P376** Securities Account Identification: SECACCCSDPXXYYAAA

**P377** Negative position flag: true

**P379** Message Instance

**P380** <Document>

**P381** 	<SctiesAcctModReq>

**P382** 		<MsgHdr>

**P383** 			<MsgId>SAMPLESACUPDATE</MsgId>

**P384** 		</MsgHdr>	

**P385** 		<AcctId>

**P386** 			<Id>SECACCCSDPXXYYAAA</Id>

**P387** 		</AcctId>

**P388** 		<Mod>

**P389** 			<ScpIndctn>UPDT</ScpIndctn>

**P390** 			<ReqdMod>

**P391** 				<SysSctiesAcct>

**P392** 					<NegPos>true</NegPos>

**P393** 				</SysSctiesAcct>

**P394** 			</ReqdMod>

**P395** 		</Mod>

**P396** 	</SctiesAcctModReq>

**P397** </Document>

