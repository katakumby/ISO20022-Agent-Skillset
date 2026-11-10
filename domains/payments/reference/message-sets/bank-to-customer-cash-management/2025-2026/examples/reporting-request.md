---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "needs-review"
title: "Account reporting request"
domain: "payments"
source_ids: ["src-000004"]
message_sets: ["bank-to-customer-cash-management"]
message_ids: ["camt.060.001.07"]
source_locations: [{"source_id": "src-000004", "locator": "Business Examples; narrative P517; T21; XML P520-P551"}, {"source_id": "src-000004", "locator": "Word file/printed pages39,40"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading paragraph indentation removed only."
limitations: ["Original fragments lack namespace/Document envelope; validation of a derived envelope is separately recorded.", "Source narrative/data/example conflicts are preserved under issue-000060."]
issue_ids: ["issue-000060"]
source_text_visual_review: "pass"
review_date: "2026-11-09"
derived_envelope_xsd_check: {"result": "pass", "source_schema_id": "src-000010", "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.060.001.07", "transform": "Assigned the supplied exact namespace to all payload tags and enclosed it in Document; interior values and structure unchanged. Original fragment retained.", "errors": []}
source_editions: ["March 2026"]
---

# Account reporting request

[src-000004](../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart1_BankToCustomerCashManagement_2025_2026_v2.docx); P517; T21; XML P520-P551.

On 27 October 2015, AAAABEBB sends an AccountReportingRequest message to its account servicer BBBBUS33 to request a BankToCustomerStatement for that day.

[Complete business-data table](../documents/src-000004/tables/tbl-0021.md)

```xml
<AcctRptgReq>
	<GrpHdr>
		<MsgId>EXAMPLE camt.060</MsgId>
		<CreDtTm>2015-10-27T17:15:00</CreDtTm>
	</GrpHdr>
	<RptgReq>
		<ReqdMsgNmId>camt.052.001.08</ReqdMsgNmId>
		<Acct>
			<Id>
				<Othr>
					<Id>310141014141</Id>
				</Othr>
			</Id>
		</Acct>
		<AcctOwnr>
			<Agt>
				<FinInstnId>
					<BICFI>AAAABEBB</BICFI>
				</FinInstnId>
			</Agt>
		</AcctOwnr>
		<RptgPrd>
			<FrToDt>
				<FrDt>2015-10-27</FrDt>
			</FrToDt>
			<FrToTm>
				<FrTm>07:30:00</FrTm>
			</FrToTm>
			<Tp>ALLL</Tp>
		</RptgPrd>
	</RptgReq>
</AcctRptgReq>
```

## Actual review and validation

Original payload pages compared2026-11-09: [39](../../../../../assets/src-000004/source-page-renders/word-page-39.png), [40](../../../../../assets/src-000004/source-page-renders/word-page-40.png). Every paragraph independently matches the Word PDF. Original fragment is well-formed; a derived exact-namespace Document wrapper passes the supplied exact XSD. Interior values and structure are unchanged. [Unresolved business/data/example discrepancies](../source-consistency.md) remain distinct from schema validity.
