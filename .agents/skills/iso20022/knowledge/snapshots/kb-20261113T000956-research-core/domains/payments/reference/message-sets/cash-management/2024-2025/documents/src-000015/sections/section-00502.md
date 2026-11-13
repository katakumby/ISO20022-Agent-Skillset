---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["27 camt.049.001.07 DeleteReservationV07", "27.2 Structure"]
file_pages: [664]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.049.001.07"]
---

# 27.2 Structure

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 664 to 664.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 664

```text
27.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <DelRsvatn> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 664
   CurrentReservation <CurRsvatn> [0..1]  665
     ReservationIdentification <RsvatnId> [0..1] Text 665
     SystemIdentification <SysId> [0..1] ± 665
     Type <Tp> [1..1]  665
{Or       Code <Cd> [1..1] CodeSet 666
Or}       Proprietary <Prtry> [1..1] Text 666
     AccountOwner <AcctOwnr> [0..1] ± 666
     AccountIdentification <AcctId> [0..1] ± 667
   SupplementaryData <SplmtryData> [0..*] ± C4 667
27.3 Constraints
C1 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C4 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
27.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
27.4.1 MessageHeader <MsgHdr>
Presence: [1..1]
Definition: Common business identification for the message.
Approved by the Payments SEG on 04 February 2025 camt.049.001.07 DeleteReservationV07
Cash Management - Maintenance 2024 - 2025 664 February 2025
```

