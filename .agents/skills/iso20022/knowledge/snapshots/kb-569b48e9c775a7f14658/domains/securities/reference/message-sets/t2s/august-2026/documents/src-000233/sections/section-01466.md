---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["37 reda.017.001.02 PartyReportV02", "37.3 Constraints"]
file_pages: [2080]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.017.001.02"]
---

# 37.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2080 to 2080.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2080

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
             ValidFrom <VldFr> [0..1] Date 2094
             Status <Sts> [1..1] CodeSet 2094
             LockReason <LckRsn> [0..*] Text 2094
           Restriction <Rstrctn> [0..*]  2095
             ValidFrom <VldFr> [1..1] DateTime 2095
             ValidTo <VldTo> [0..1] DateTime 2095
             Type <Tp> [1..1] Text 2095
Or}         BusinessError <BizErr> [1..*]  2095
           Error <Err> [1..1]  2095
{Or             Code <Cd> [1..1] CodeSet 2096
Or}             Proprietary <Prtry> [1..1] Text 2096
           Description <Desc> [0..1] Text 2096
Or}     OperationalError <OprlErr> [1..*]  2096
       Error <Err> [1..1]  2097
{Or         Code <Cd> [1..1] CodeSet 2097
Or}         Proprietary <Prtry> [1..1] Text 2097
       Description <Desc> [0..1] Text 2097
   SupplementaryData <SplmtryData> [0..*] ± C4 2097
37.3 Constraints
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.017.001.02 PartyReportV02
Target2-Securities 2080 August 2026
```

