---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.7.3 CounterpartyReference <CtrPtyRef>"]
file_pages: [626]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.7.3 CounterpartyReference <CtrPtyRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 626 to 626.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 626

```text
ClientReference <ClntRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
28.4.7.3  CounterpartyReference <CtrPtyRef>
Presence: [0..1]
Definition: Unambiguous identification of the transfer allocated by the counterparty.
CounterpartyReference <CtrPtyRef> contains the following elements (see "AdditionalReference10"
on page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
28.4.7.4  BusinessFlowType <BizFlowTp>
Presence: [0..1]
Definition: Identifies the business process in which the actors are involved. This is important to trigger
the right business process, according to the market business model, which may require matching
instructions in a CSD environment (double leg process) or not (single leg process).
Datatype: "BusinessFlowType1Code" on page 5279
CodeName Name Definition
SLDP SingleLegDeliveringParty Single leg process initiated by the
delivering party.
SLRP SingleLegReceivingParty Single leg process initiated by the
receiving party.
DLPR DoubleLegProcess Double leg process.
28.4.7.5  RequestedTransferDate <ReqdTrfDt>
Presence: [0..1]
Definition: Date for which the instructing party requests the transfer.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 626 May 2026
```

