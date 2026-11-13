---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
message_ids: ["reda.037.001.01"]
source_locations: [{"source_id": "src-000371", "heading_path": ["Business Examples", "Securities Account Audit Trail Report - reda.037.001.01"], "first_paragraph": "P633", "last_paragraph": "P665", "rendered_file_pages": [40, 41]}]
issue_ids: []
limitations: ["The original has no namespace. Schema-validation results refer only to the explicitly derived namespace-assigned copy; the literal source XML is unchanged."]
---

# Securities Account Audit Trail Report - reda.037.001.01

[src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; P633–P665; Word file pages 40–41. This is the literal source example. Original XML is retained without a namespace; schema testing below uses only an explicitly derived namespace assignment.

**P634** Description

**P635** The following Securities Account Audit Trail Report represents the answer to the Securities Account Audit Trail Query described in the chapter 7.8. In this case, the securities account with identification SECACCCSDPXXYYAAA had only one change performed by the user USER1 and approved by the user USER2 on 2019-01-03T17:59:00 regarding the change of the Negative Position from the value False to the new value True. 

**P636** Message Instance

**P637–P664**

```xml
<Document>
	<SctiesAcctAudtTrlRpt>
		 <MsgHdr>
			<MsgId>NONREF</MsgId>
			<OrgnlBizInstr>
				<MsgId>SAMPLESACATRQUE</MsgId>
			</OrgnlBizInstr>
		</MsgHdr>
		<RptOrErr>
			<SctiesAcctAudtTrlRpt>
				<SctiesAcctAudtTrlOrErr>
					<AudtTrl>
						<FldNm>NegativePosition</FldNm>
						<OdFldVal>False</OdFldVal>
						<NewFldVal>True</NewFldVal>
						<OprTmStmp>2019-01-03T17:59:00</OprTmStmp>
						<InstgUsr>USER1</InstgUsr>
						<ApprvgUsr>USER2</ApprvgUsr>
					</AudtTrl>
				</SctiesAcctAudtTrlOrErr>
				<SctiesAcctId>
					<Id>SECACCCSDPXXYYAAA</Id>
				</SctiesAcctId>
			</SctiesAcctAudtTrlRpt>
		</RptOrErr>
	</SctiesAcctAudtTrlRpt>
</Document>

```


## Validation

| Paragraphs | XML syntax | Namespace-only derived schema validation |
| --- | --- | --- |
| P637–P664 | pass | pass |


[reda.037.001.01](../../../../messages/reda.037.001.01/index.md) · [Exact derivation and error evidence](../../../../../../../evidence/archived/1371923b3cb2b1a498b71abb.md)
