---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.9.2 TransferorRegisteredAccount <TrfrRegdAcct>", "28.4.9.2.1 Identification <Id>"]
file_pages: [674]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.9.2.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 674 to 674.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 674

```text
TransferorRegisteredAccount <TrfrRegdAcct> contains the following Account38 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 674
   AccountName <AcctNm> [0..1] Text 674
   Designation <Dsgnt> [0..1] Text 674
   Servicer <Svcr> [0..1] ± 674
   SubAccountDetails <SubAcctDtls> [0..1] ± 674
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 675
28.4.9.2.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
28.4.9.2.2  AccountName <AcctNm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
28.4.9.2.3  Designation <Dsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled
individually.
Datatype: "Max35Text" on page 5403
28.4.9.2.4  Servicer <Svcr>
Presence: [0..1]
Definition: Institution that maintains the records where the account is held.
Servicer <Svcr> contains the following elements (see "PartyIdentification139" on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
28.4.9.2.5  SubAccountDetails <SubAcctDtls>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 674 May 2026
```

