---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
message_ids: ["reda.019.001.01"]
source_locations: [{"source_id": "src-000371", "heading_path": ["Business Examples", "Securities Account Query - reda.019.001.01"], "first_paragraph": "P496", "last_paragraph": "P523", "rendered_file_pages": [36, 37]}]
issue_ids: []
limitations: ["The original has no namespace. Schema-validation results refer only to the explicitly derived namespace-assigned copy; the literal source XML is unchanged."]
---

# Securities Account Query - reda.019.001.01

[src-000371](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; P496–P523; Word file pages 36–37. This is the literal source example. Original XML is retained without a namespace; schema testing below uses only an explicitly derived namespace assignment.

**P497** Description

**P498** The Securities Account Query message can be used to perform the following queries:

**P499** Securities Account Reference Data Query;

**P500** Securities Account List Query.

**P501** In this example the Party CSDAXXYYAAA perform a Securities Account List Query to request a list of securities account.

**P502** Message Instance

**P503–P523**

```xml
<Document>
	<SctiesAcctQry>
		<MsgHdr>
			<MsgId>SAMPLESALIQUERY</MsgId>
			<ReqTp>
				<Prtry>
					<Id>SALI</Id>
					<SchmeNm>SACQ</SchmeNm>
					<Issr>T2S</Issr>
				</Prtry>
			</ReqTp>
		</MsgHdr>
		<SchCrit>
			<AcctSvcr>
				<Id>
					<AnyBIC>CSDAXXYYAAA</AnyBIC>
				</Id>
			</AcctSvcr>
		</SchCrit>
	</SctiesAcctQry>
</Document>
```


## Validation

| Paragraphs | XML syntax | Namespace-only derived schema validation |
| --- | --- | --- |
| P503–P523 | pass | pass |


[reda.019.001.01](../../../../messages/reda.019.001.01/index.md) · [Exact derivation and error evidence](../../../../../../../tracking/reviews/t2s-securities-account-reference-data.json)
