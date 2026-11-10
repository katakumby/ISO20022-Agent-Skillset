---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
message_ids: ["reda.036.001.01"]
source_locations: [{"source_id": "src-000371", "heading_path": ["Business Examples", "Securities Account Audit Trail Query - reda.036.001.01"], "first_paragraph": "P611", "last_paragraph": "P632", "rendered_file_pages": [40]}]
issue_ids: []
limitations: ["The original has no namespace. Schema-validation results refer only to the explicitly derived namespace-assigned copy; the literal source XML is unchanged."]
---

# Securities Account Audit Trail Query - reda.036.001.01

[src-000371](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; P611–P632; Word file pages 40–40. This is the literal source example. Original XML is retained without a namespace; schema testing below uses only an explicitly derived namespace assignment.

**P612** Description

**P613** The following Securities Account Audit Trail Query message is used to query all the audit trail records regarding the securities account with identification SECACCCSDPXXYYAAA in the period between 2019-01-01 and 2019-01-05.

**P614** Message Instance

**P615–P632**

```xml
<Document>
	<SctiesAcctAudtTrlQry>
		<MsgHdr>
			<MsgId>SAMPLESACATRQUE</MsgId>
		</MsgHdr>
		<SchCrit>
			<SctiesAcctId>
				<Id>SECACCCSDPXXYYAAA</Id>
			</SctiesAcctId>
			<DtPrd>
			<FrToDt>
			<FrDt>2019-01-01</FrDt>
			<ToDt>2019-01-05</ToDt>
			</FrToDt>
			</DtPrd>
		</SchCrit>
	</SctiesAcctAudtTrlQry>
</Document>
```


## Validation

| Paragraphs | XML syntax | Namespace-only derived schema validation |
| --- | --- | --- |
| P615–P632 | pass | pass |


[reda.036.001.01](../../../../messages/reda.036.001.01/index.md) · [Exact derivation and error evidence](../../../../../../../tracking/reviews/t2s-securities-account-reference-data.json)
