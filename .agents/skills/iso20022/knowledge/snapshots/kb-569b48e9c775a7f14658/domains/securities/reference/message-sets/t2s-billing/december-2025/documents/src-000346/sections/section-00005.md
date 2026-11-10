---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["2 camt.076.001.01 BillingReportRequestV01", "2.2 Structure"]
file_pages: [5]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.076.001.01"]
---

# 2.2 Structure

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 5 to 5.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <BllgRptReq> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 6
   SearchCriteria <SchCrit> [1..*]  6
     Service <Svc> [0..1]  7
       SystemIdentification <SysId> [1..1] ± 7
       SystemCurrency <SysCcy> [0..1] CodeSet C1 7
     BillingIdentification <BllgId> [0..1] Text 8
     BillingPeriod <BllgPrd> [0..1] ± 8
     ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 8
     PartyIdentification <PtyId> [0..1] ± 8
     AccountIdentification <AcctId> [0..1]  9
{Or       SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 9
Or}       CashAccountIdentification <CshAcctId> [1..1] ± 9
   SupplementaryData <SplmtryData> [0..*] ± C5 9
2.3 Constraints
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
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
camt.076.001.01 BillingReportRequestV01
Target2-Securities - Billing 5 December 2025
```

