---
template: false
document_kind: "source-example"
review_status: "reviewed"
domain: "securities"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_sets: ["t2s-securities-account-reference-data"]
message_ids: ["reda.032.001.01"]
source_locations: [{"source_id": "src-000371", "heading_path": ["Business Examples", "Securities Account Deletion Request - reda.032.001.01"], "first_paragraph": "P398", "last_paragraph": "P413", "rendered_file_pages": [34]}]
issue_ids: []
limitations: ["The original has no namespace. Schema-validation results refer only to the explicitly derived namespace-assigned copy; the literal source XML is unchanged."]
---

# Securities Account Deletion Request - reda.032.001.01

[src-000371](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`; P398–P413; Word file pages 34–34. This is the literal source example. Original XML is retained without a namespace; schema testing below uses only an explicitly derived namespace assignment.

**P399** Description

**P400** This example message is sent in order to delete the securities account SECACCCSDPXXYYAAA:

**P401** Securities Account Identification: SECACCCSDPXXYYAAA

**P402** Message Instance

**P403–P412**

```xml
<Document>
	<SctiesAcctDeltnReq>
		<MsgHdr>
			<MsgId>SAMPLESACDELETE</MsgId>
		</MsgHdr>
		<AcctId>
			<Id>SECACCCSDPXXYYAAA</Id>
		</AcctId>
	</SctiesAcctDeltnReq>
</Document>
```


## Validation

| Paragraphs | XML syntax | Namespace-only derived schema validation |
| --- | --- | --- |
| P403–P412 | pass | pass |


[reda.032.001.01](../../../../messages/reda.032.001.01/index.md) · [Exact derivation and error evidence](../../../../../../../tracking/reviews/t2s-securities-account-reference-data.json)
