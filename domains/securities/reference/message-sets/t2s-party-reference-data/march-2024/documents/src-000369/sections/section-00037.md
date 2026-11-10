---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 reda.017.001.02 PartyReportV02", "5.3 Constraints"]
file_pages: [43]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 5.3 Constraints

Source: [src-000369](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 43 to 43.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             ValidFrom <VldFr> [0..1] Date 57
             Status <Sts> [1..1] CodeSet 57
             LockReason <LckRsn> [0..*] Text 57
           Restriction <Rstrctn> [0..*]  58
             ValidFrom <VldFr> [1..1] DateTime 58
             ValidTo <VldTo> [0..1] DateTime 58
             Type <Tp> [1..1] Text 58
Or}         BusinessError <BizErr> [1..*]  58
           Error <Err> [1..1]  58
{Or             Code <Cd> [1..1] CodeSet 59
Or}             Proprietary <Prtry> [1..1] Text 59
           Description <Desc> [0..1] Text 59
Or}     OperationalError <OprlErr> [1..*]  59
       Error <Err> [1..1]  60
{Or         Code <Cd> [1..1] CodeSet 60
Or}         Proprietary <Prtry> [1..1] Text 60
       Description <Desc> [0..1] Text 60
   SupplementaryData <SplmtryData> [0..*] ± C4 60
5.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.017.001.02 PartyReportV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
43 March 2024
```

