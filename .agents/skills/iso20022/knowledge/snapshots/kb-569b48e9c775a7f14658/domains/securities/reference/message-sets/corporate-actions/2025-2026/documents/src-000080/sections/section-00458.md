---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.18 ReceivingSettlementParties <RcvgSttlmPties>"]
file_pages: [612]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.18 ReceivingSettlementParties <RcvgSttlmPties>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 612 to 612.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 612

```text
8.4.12.10.18  ReceivingSettlementParties <RcvgSttlmPties>
Presence: [0..1]
Definition: Identifies the chain of receiving settlement parties.
Impacted by: C50 "Party2PresenceRule", C51 "Party3PresenceRule"
ReceivingSettlementParties <RcvgSttlmPties> contains the following elements (see
"SettlementParties129" on page 1133 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1]  C3 1134
     Identification <Id> [1..1]  1135
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1135
Or       NameAndAddress <NmAndAdr> [1..1] ± 1136
Or       Country <Ctry> [1..1] CodeSet C3 1136
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1136
     ProcessingIdentification <PrcgId> [0..1] Text 1136
     AlternateIdentification <AltrnId> [0..*] ± 1136
   Party1 <Pty1> [0..1] ± C4, C54,
C56,
C58
1137
   Party2 <Pty2> [0..1] ± C4, C54,
C56,
C58
1138
   Party3 <Pty3> [0..1] ± C4, C54,
C56,
C58
1139
Constraints
• Party2PresenceRule
If Party 2 is present, then Party 1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party 3 is present, then Party 2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
8.4.12.10.19  DeliveringSettlementParties <DlvrgSttlmPties>
Presence: [0..1]
Definition: Identifies the chain of delivering settlement parties.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 612 February 2026
```

