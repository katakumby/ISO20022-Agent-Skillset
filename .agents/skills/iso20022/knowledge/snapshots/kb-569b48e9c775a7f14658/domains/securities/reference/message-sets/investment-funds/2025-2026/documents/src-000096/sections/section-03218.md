---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.10 Clearing System Member Identification"]
file_pages: [4454]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.10 Clearing System Member Identification

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4454 to 4454.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4454

```text
PayeeIdentification <PyeeId> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
66.1.10 Clearing System Member Identification
66.1.10.1  ClearingSystemMemberIdentification4Choice
Definition: Choice of identifiers for a clearing system member, as assigned by the clearing system. In
some clearing systems, the accounts of the clearing system members are also assigned an identifier.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CHIPSUniversalIdentification <USCHU> [1..1] IdentifierSet 4454
Or   NewZealandNCCIdentification <NZNCC> [1..1] IdentifierSet 4455
Or   IrishNSCIdentification <IENSC> [1..1] IdentifierSet 4455
Or   UKDomesticSortCode <GBSC> [1..1] IdentifierSet 4455
Or   CHIPSParticipantIdentification <USCH> [1..1] IdentifierSet 4455
Or   SwissBCIdentification <CHBC> [1..1] IdentifierSet 4455
Or   FedwireRoutingNumberIdentification <USFW> [1..1] IdentifierSet 4455
Or   PortugueseNCCIdentification <PTNCC> [1..1] IdentifierSet 4455
Or   RussianCentralBankIdentificationCode <RUCB> [1..1] IdentifierSet 4456
Or   ItalianDomesticIdentificationCode <ITNCC> [1..1] IdentifierSet 4456
Or   AustrianBankleitzahlIdentification <ATBLZ> [1..1] IdentifierSet 4456
Or   CanadianPaymentsAssociationRoutingNumberIdentificati
on <CACPA>
[1..1] IdentifierSet 4456
Or   SwissSICIdentification <CHSIC> [1..1] IdentifierSet 4456
Or   GermanBankleitzahlIdentification <DEBLZ> [1..1] IdentifierSet 4456
Or   SpanishDomesticInterbankingIdentification <ESNCC> [1..1] IdentifierSet 4456
Or   SouthAfricanNCCIdentification <ZANCC> [1..1] IdentifierSet 4457
Or   HongKongBankCode <HKNCC> [1..1] IdentifierSet 4457
Or   AustralianExtensiveBranchNetworkIdentification
<AUBSBx>
[1..1] IdentifierSet 4457
Or}   AustralianSmallNetworkIdentification <AUBSBs> [1..1] IdentifierSet 4457
66.1.10.1.1  CHIPSUniversalIdentification <USCHU>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4454 May 2026
```

