---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.38 PartyIdentification132", "66.1.30.38.3 NameAndAddress <NmAndAdr>"]
file_pages: [5030]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.38.3 NameAndAddress <NmAndAdr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5030 to 5030.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5030

```text
Definition: Choice of identifier for a clearing system member, as assigned by the clearing system. In
some clearing systems, the accounts of the clearing system members are also assigned an identifier.
ClearingSystemMemberIdentification <ClrSysMmbId> contains one of the following elements (see
"ClearingSystemMemberIdentification2Choice" on page 4457 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CHIPSUniversalIdentification <USCHU> [1..1] IdentifierSet 4458
Or   NewZealandNCCIdentification <NZNCC> [1..1] IdentifierSet 4458
Or   IrishNSCIdentification <IENSC> [1..1] IdentifierSet 4459
Or   UKDomesticSortCode <GBSC> [1..1] IdentifierSet 4459
Or   CHIPSParticipantIdentification <USCH> [1..1] IdentifierSet 4459
Or   SwissBCIdentification <CHBC> [1..1] IdentifierSet 4459
Or   FedwireRoutingNumberIdentification <USFW> [1..1] IdentifierSet 4459
Or   PortugueseNCCIdentification <PTNCC> [1..1] IdentifierSet 4459
Or   RussianCentralBankIdentificationCode <RUCB> [1..1] IdentifierSet 4459
Or   ItalianDomesticIdentificationCode <ITNCC> [1..1] IdentifierSet 4460
Or   AustrianBankleitzahlIdentification <ATBLZ> [1..1] IdentifierSet 4460
Or   CanadianPaymentsAssociationRoutingNumberIdentificati
on <CACPA>
[1..1] IdentifierSet 4460
Or   SwissSICIdentification <CHSIC> [1..1] IdentifierSet 4460
Or   GermanBankleitzahlIdentification <DEBLZ> [1..1] IdentifierSet 4460
Or   SpanishDomesticInterbankingIdentification <ESNCC> [1..1] IdentifierSet 4460
Or   SouthAfricanNCCIdentification <ZANCC> [1..1] IdentifierSet 4460
Or   HongKongBankCode <HKNCC> [1..1] IdentifierSet 4461
Or   AustralianExtensiveBranchNetworkIdentification
<AUBSBx>
[1..1] IdentifierSet 4461
Or   AustralianSmallNetworkIdentification <AUBSBs> [1..1] IdentifierSet 4461
Or   IndianFinancialSystemCode <INIFSC> [1..1] IdentifierSet 4461
Or   HellenicBankIdentificationCode <GRHEBIC> [1..1] IdentifierSet 4461
Or   PolishNationalClearingCode <PLKNR> [1..1] IdentifierSet 4461
Or}   OtherClearingCodeIdentification <OthrClrCdId> [1..1] Text 4462
66.1.30.38.3  NameAndAddress <NmAndAdr>
Presence: [0..1]
Definition: Name and address of the party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5030 May 2026
```

