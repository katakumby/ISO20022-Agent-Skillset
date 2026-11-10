---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["26 camt.048.001.07 ModifyReservationV07", "26.2 Structure"]
file_pages: [655]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.048.001.07"]
---

# 26.2 Structure

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 655 to 655.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 655

```text
26.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ModfyRsvatn> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 656
   ReservationIdentification <RsvatnId> [1..1]  656
{Or     Current <Cur> [1..1]  657
       ReservationIdentification <RsvatnId> [0..1] Text 658
       SystemIdentification <SysId> [0..1] ± 658
       Type <Tp> [1..1]  658
{Or         Code <Cd> [1..1] CodeSet 658
Or}         Proprietary <Prtry> [1..1] Text 658
       AccountOwner <AcctOwnr> [0..1] ± 658
       AccountIdentification <AcctId> [0..1] ± 659
Or}     Default <Dflt> [1..1]  659
       ReservationIdentification <RsvatnId> [0..1] Text 660
       SystemIdentification <SysId> [0..1] ± 660
       Type <Tp> [1..1]  660
{Or         Code <Cd> [1..1] CodeSet 660
Or}         Proprietary <Prtry> [1..1] Text 661
       AccountOwner <AcctOwnr> [0..1] ± 661
       AccountIdentification <AcctId> [0..1] ± 661
   NewReservationValueSet <NewRsvatnValSet> [1..1] ± 661
   SupplementaryData <SplmtryData> [0..*] ± C6 662
26.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
Approved by the Payments SEG on 04 February 2025 camt.048.001.07 ModifyReservationV07
Cash Management - Maintenance 2024 - 2025 655 February 2025
```

