---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.8 Account <Acct>", "8.4.12.11.8.2 ChargesAccount <ChrgsAcct>"]
file_pages: [621]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.8.2 ChargesAccount <ChrgsAcct>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 621 to 621.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 621

```text
8.4.12.11.8.2  ChargesAccount <ChrgsAcct>
Presence: [1..1]
Definition: Account to be used for charges if different from the account for payment.
ChargesAccount <ChrgsAcct> contains one of the following elements (see
"CashAccountIdentification5Choice" on page 830 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C16 830
Or}   Proprietary <Prtry> [1..1] Text 831
8.4.12.11.8.3  TaxAccount <TaxAcct>
Presence: [1..1]
Definition: Account to be used for taxes if different from the account for payment.
TaxAccount <TaxAcct> contains one of the following elements (see
"CashAccountIdentification5Choice" on page 830 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C16 830
Or}   Proprietary <Prtry> [1..1] Text 831
8.4.12.11.9  CashParties <CshPties>
Presence: [0..1]
Definition: Provides information about cash parties.
CashParties <CshPties> contains the following elements (see "CashParties43" on page 1034 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Creditor <Cdtr> [0..1]  C5 1034
     Identification <Id> [1..1] ± 1034
     CashAccount <CshAcct> [0..1] ± 1035
     ProcessingIdentification <PrcgId> [0..1] Text 1035
     AlternateIdentification <AltrnId> [0..1] ± 1035
   CreditorAgent <CdtrAgt> [0..1] ± C6 1035
   MarketClaimCounterparty <MktClmCtrPty> [0..1]  C5 1036
     Identification <Id> [1..1] ± 1036
     CashAccount <CshAcct> [0..1] ± 1037
     ProcessingIdentification <PrcgId> [0..1] Text 1037
     AlternateIdentification <AltrnId> [0..1] ± 1037
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 621 February 2026
```

