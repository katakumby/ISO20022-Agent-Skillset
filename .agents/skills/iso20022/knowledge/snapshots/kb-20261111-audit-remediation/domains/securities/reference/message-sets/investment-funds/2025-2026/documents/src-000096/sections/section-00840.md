---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.5 Portfolio <Prtfl>", "36.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>", "36.4.15.5.1.15 InvestorTaxReference <InvstrTaxRef>", "36.4.15.5.1.15.1 Type <Tp>", "36.4.15.5.1.15.1.2 Proprietary <Prtry>"]
file_pages: [1165]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.5.1.15.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1165 to 1165.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1165

```text
Datatype: "PersonIdentificationType7Code" on page 5341
CodeName Name Definition
ATIN AdoptionTaxpayerIdentificationNumber Temporary tax processing number (used
in the domestic adoption of a child).
GTIN GenericTaxIdentificationNumber Generic tax identification number.
ITIN IndividualTaxpayerIdentificationNumber Tax processing number.
36.4.15.5.1.15.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of tax reference expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
36.4.15.5.1.15.2  Reference <Ref>
Presence: [1..1]
Definition: Pension scheme tax reference issued to the pension plan by a central organisation.
Datatype: "Max35Text" on page 5403
36.4.15.5.1.16  InvestmentsToFollowValue <InvstmtsToFllwVal>
Presence: [0..*]
Definition: Value of the investments to follow.
InvestmentsToFollowValue <InvstmtsToFllwVal> contains the following elements (see
"DateAndAmount2" on page 4343 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [0..1] Date 4343
   Amount <Amt> [1..1] Amount C2, C10 4343
36.4.15.5.1.17  InnovativeFinance <InnvtvFinc>
Presence: [0..*]
Definition: Information about an innovative finance product.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1165 May 2026
```

