---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["23 camt.025.001.09 ReceiptV09", "23.3 Constraints"]
file_pages: [606]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.025.001.09"]
---

# 23.3 Constraints

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 606 to 606.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 606

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         InterbankSettlementDate <IntrBkSttlmDt> [1..1] Date 617
         InstructingAgent <InstgAgt> [1..1] ± 617
Or}       ProprietaryIdentification <PrtryId> [1..1] Text 618
     RequestHandling <ReqHdlg> [0..*]  C4 618
       Status <Sts> [1..1]  619
{Or         Code <Cd> [1..1] CodeSet 619
Or}         Proprietary <Prtry> [1..1] Text 619
       StatusReason <StsRsn> [0..1]  C5 620
         Originator <Orgtr> [0..1] ± 620
         Reason <Rsn> [0..1]  621
{Or           Code <Cd> [1..1] CodeSet 622
Or}           Proprietary <Prtry> [1..1] Text 622
         AdditionalInformation <AddtlInf> [0..*] Text 622
       Description <Desc> [0..1] Text 622
   SupplementaryData <SplmtryData> [0..*] ± C6 622
23.3 Constraints
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
C4 DescriptionRule
If Description is present, then Status/Code is not allowed.
C5 StatusReasonRule
If Reason/Code is equal to NARR, then AddititionalInformation must be present.
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 606 February 2025
```

