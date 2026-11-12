---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.11 PartyIdentificationAndAccount199", "35.1.18.11.2 LEI <LEI>"]
file_pages: [1679]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.11.2 LEI <LEI>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1679 to 1679.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1679

```text
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 1689 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1689
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1689
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1690
35.1.18.11.2  LEI <LEI>
Presence: [0..1]
Definition: Legal Entity Identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 2187
35.1.18.11.3  AlternateIdentification <AltrnId>
Presence: [0..1]
Definition: Alternate identification for a party.
AlternateIdentification <AltrnId> contains the following elements (see "AlternatePartyIdentification7"
on page 1691 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationType <IdTp> [1..1] ± 1691
   Country <Ctry> [1..1] CodeSet C7 1691
   AlternateIdentification <AltrnId> [1..1] Text 1691
35.1.18.11.4  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount22" on
page 1344 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1344
   Type <Tp> [0..1] ± 1344
   Name <Nm> [0..1] Text 1344
35.1.18.11.5  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1679 March 2026
```

