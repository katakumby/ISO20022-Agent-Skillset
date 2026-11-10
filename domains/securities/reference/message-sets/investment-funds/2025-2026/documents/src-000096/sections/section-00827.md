---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.1 MasterReference <MstrRef>"]
file_pages: [1148]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1148 to 1148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1148

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Party4 <Pty4> [0..1] ± 1294
         Party5 <Pty5> [0..1] ± 1295
       DeliveringSideDetails <DlvrgSdDtls> [0..1]  C12,
C20,
C38,
C39,
C40,
C41,
C47
1295
         Depository <Dpstry> [0..1] ± 1297
         Party1 <Pty1> [0..1] ± 1298
         Party2 <Pty2> [0..1] ± 1298
         Party3 <Pty3> [0..1] ± 1298
         Party4 <Pty4> [0..1] ± 1299
         Party5 <Pty5> [0..1] ± 1299
     AssetsHeldInOwnName <AsstsHeldInOwnNm> [0..1] Indicator 1300
     TransferResultsInChangeOfBeneficialOwner
<TrfRsltsInChngOfBnfclOwnr>
[0..1] Indicator 1300
     AdditionalInformation <AddtlInf> [0..*] ± 1300
   AdditionalInformation <AddtlInf> [0..*] ± 1300
36.4.15.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual transfers as assigned by the
instructing party. This identifier links the individual transfers together.
Datatype: "Max35Text" on page 5403
36.4.15.2  TransferInstructionReference <TrfInstrRef>
Presence: [1..1]
Definition: Identification assigned to the transfer of assets.
Datatype: "Max35Text" on page 5403
36.4.15.3  TransferConfirmationIdentification <TrfConfId>
Presence: [1..1]
Definition: Identification of the confirmation assigned by the transferor to the transfer.
Datatype: "Max35Text" on page 5403
36.4.15.4  ActualTransferDate <ActlTrfDt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1148 May 2026
```

