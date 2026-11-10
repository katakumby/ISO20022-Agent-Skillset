---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.1 MasterReference <MstrRef>"]
file_pages: [1531]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1531 to 1531.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1531

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Party4 <Pty4> [0..1] ± 1677
         Party5 <Pty5> [0..1] ± 1678
       DeliveringSideDetails <DlvrgSdDtls> [0..1]  C12,
C20,
C38,
C39,
C40,
C41,
C47
1678
         Depository <Dpstry> [0..1] ± 1680
         Party1 <Pty1> [0..1] ± 1681
         Party2 <Pty2> [0..1] ± 1681
         Party3 <Pty3> [0..1] ± 1681
         Party4 <Pty4> [0..1] ± 1682
         Party5 <Pty5> [0..1] ± 1682
     AssetsHeldInOwnName <AsstsHeldInOwnNm> [0..1] Indicator 1683
     TransferResultsInChangeOfBeneficialOwner
<TrfRsltsInChngOfBnfclOwnr>
[0..1] Indicator 1683
     AdditionalInformation <AddtlInf> [0..*] ± 1683
   AdditionalInformation <AddtlInf> [0..*] ± 1683
40.4.15.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
40.4.15.2  TransferInstructionReference <TrfInstrRef>
Presence: [1..1]
Definition: Identification assigned to the transfer of assets.
Datatype: "Max35Text" on page 5403
40.4.15.3  TransferCompletionIdentification <TrfCmpltnId>
Presence: [1..1]
Definition: Identification of the completion assigned by the transferor to the transfer.
Datatype: "Max35Text" on page 5403
40.4.15.4  ActualTransferDate <ActlTrfDt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1531 May 2026
```

