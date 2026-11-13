---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13", "15.4 Message Building Blocks"]
file_pages: [817]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.044.001.13"]
preceding_topic_continuations: [{"constraint_ids": ["C9", "C10", "C11", "C12", "C13", "C14", "C15"], "until_heading": "15.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 817, "topic": "15.3 Constraints", "reference_path": "domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00625.md"}]
---

# 15.4 Message Building Blocks

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 817 to 817.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 817, C9–C15 before **15.4 Message Building Blocks** continue [15.3 Constraints](section-00625.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 817

```text
(COAF). Those recommendations are available in the SMPG Global Market Practices Part 1
document on www.smpg.info.
C9 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C10 SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C11 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
C12 SafekeepingAccountOrBlockChainAddress3Rule
If SafekeepingAccount is present, then BlockChainAddressOrWallet must be absent.
C13 SafekeepingPlaceRule
The SafekeepingPlace is only to be used by global custodians that allow their clients to specify
where the securities are to be held, for example, in an ICSD account versus an account at the
local CSD.
C14 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C15 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
15.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
15.4.1 MovementPreliminaryAdviceIdentification
<MvmntPrlimryAdvcId>
Presence: [1..1]
Definition: Identification of a previously sent movement preliminary advice document.
MovementPreliminaryAdviceIdentification <MvmntPrlimryAdvcId> contains the following elements
(see "DocumentIdentification31" on page 860 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 861
   LinkageType <LkgTp> [0..1] ± C22 861
Approved by the Securities SEG on 27 January 2026 seev.044.001.13
CorporateActionMovementPreliminaryAdviceCancel
lationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 817 February 2026
```

