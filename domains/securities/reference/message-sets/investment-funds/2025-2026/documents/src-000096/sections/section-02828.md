---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.20 SubscriptionLegDetails <SbcptLegDtls>", "55.4.5.20.18 SettlementAndCustodyDetails <SttlmAndCtdyDtls>", "55.4.5.20.18.2 SettlementPlace <SttlmPlc>", "55.4.5.20.18.2.1 Party <Pty>"]
file_pages: [3973]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.20.18.2.1 Party <Pty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3973 to 3973.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3973

```text
SettlementPlace <SttlmPlc> contains the following PartyIdentification339 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1]  3973
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3973
Or     ProprietaryIdentification <PrtryId> [1..1] ± 3973
Or     NameAndAddress <NmAndAdr> [1..1] ± 3974
Or}     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3974
   LEI <LEI> [0..1] IdentifierSet 3974
55.4.5.20.18.2.1  Party <Pty>
Presence: [1..1]
Definition: Unique identification of the party.
Party <Pty> contains one of the following PartyIdentification262Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 3973
Or   ProprietaryIdentification <PrtryId> [1..1] ± 3973
Or   NameAndAddress <NmAndAdr> [1..1] ± 3974
Or}   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 3974
55.4.5.20.18.2.1.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Identification of the party expressed as a BIC.
Impacted by: C4 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 5389
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
55.4.5.20.18.2.1.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to the party using a proprietary identification
scheme.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3973 May 2026
```

