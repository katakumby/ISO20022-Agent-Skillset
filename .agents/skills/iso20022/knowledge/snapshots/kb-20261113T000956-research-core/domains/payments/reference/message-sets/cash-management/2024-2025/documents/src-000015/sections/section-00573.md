---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["33 camt.101.001.02 CreateLimitV02", "33.2 Structure"]
file_pages: [746]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.101.001.02"]
---

# 33.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 746 to 746.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 746

```text
33.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CretLmt> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 747
   LimitData <LmtData> [1..*]  747
     LimitIdentification <LmtId> [1..1]  C3, C4 748
       SystemIdentification <SysId> [0..1] ± 749
       BilateralLimitCounterpartyIdentification <BilLmtCtrPtyId> [0..1] ± 749
       Type <Tp> [1..1]  750
{Or         Code <Cd> [1..1] CodeSet 750
Or}         Proprietary <Prtry> [1..1] Text 752
       AccountOwner <AcctOwnr> [0..1] ± 752
       AccountIdentification <AcctId> [0..1] ± 752
     StartDateTime <StartDtTm> [0..1] ± 753
     Amount <Amt> [1..1] ± 753
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 753
   SupplementaryData <SplmtryData> [0..*] ± C8 753
33.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C3 BilateralLimitCounterparty1Rule
If Type is MULT, then BilateralLimitCounterpartyIdentification is not allowed.
C4 BilateralLimitCounterparty2Rule
If Type is BILI or NELI or INBI, then BilateralLimitCounterpartyIdentification must be present.
C5 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Payments SEG on 04 February 2025 camt.101.001.02 CreateLimitV02
Cash Management - Maintenance 2024 - 2025 746 February 2025
```

