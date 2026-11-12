---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["14 camt.076.001.01 BillingReportRequestV01", "14.2 Structure"]
file_pages: [234]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.076.001.01"]
---

# 14.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 234 to 234.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 234

```text
14.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <BllgRptReq> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 235
   SearchCriteria <SchCrit> [1..*]  235
     Service <Svc> [0..1]  236
       SystemIdentification <SysId> [1..1] ± 236
       SystemCurrency <SysCcy> [0..1] CodeSet C1 236
     BillingIdentification <BllgId> [0..1] Text 237
     BillingPeriod <BllgPrd> [0..1] ± 237
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 237
     PartyIdentification <PtyId> [0..1] ± 237
     AccountIdentification <AcctId> [0..1]  238
{Or       SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 238
Or}       CashAccountIdentification <CshAcctId> [1..1] ± 238
   SupplementaryData <SplmtryData> [0..*] ± C5 238
14.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.076.001.01 BillingReportRequestV01
Target2-Securities 234 August 2026
```

