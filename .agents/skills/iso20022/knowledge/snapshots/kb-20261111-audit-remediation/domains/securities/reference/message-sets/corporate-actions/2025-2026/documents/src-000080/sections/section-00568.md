---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "13.4 Message Building Blocks"]
file_pages: [739]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
preceding_topic_continuations: [{"constraint_ids": ["C22", "C23", "C24", "C25", "C26", "C27", "C28", "C29"], "until_heading": "13.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 739, "topic": "13.3 Constraints", "reference_path": "domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00567.md"}]
---

# 13.4 Message Building Blocks

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 739 to 739.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 739, C22–C29 before **13.4 Message Building Blocks** continue [13.3 Constraints](section-00567.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 739

```text
C22 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C23 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C24 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C25 SafekeepingPlaceRule
SafekeepingPlace must only be used by global custodians that allow their clients to specify
where the securities are to be held, for example, in an ICSD account versus an account at the
local CSD.
C26 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C27 StatusQuantityOrStatusCashAmount1Rule
If StatusQuantity is present, then StatusCashAmount is not allowed. (MT 567 C5).
C28 StatusQuantityOrStatusCashAmount2Rule
If StatusCashAmount is present, then StatusQuantity is not allowed. (MT 567 C5).
C29 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
13.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
13.4.1 InstructionCancellationRequestIdentification
<InstrCxlReqId>
Presence: [0..1]
Definition: Identification of a related instruction cancellation request document.
InstructionCancellationRequestIdentification <InstrCxlReqId> contains the following elements (see
"DocumentIdentification9" on page 877 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 877
13.4.2 OtherDocumentIdentification <OthrDocId>
Presence: [0..*]
Definition: Identification of other documents as well as the document number.
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 739 February 2026
```

