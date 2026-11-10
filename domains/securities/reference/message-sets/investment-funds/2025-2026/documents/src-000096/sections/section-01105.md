---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.5 Portfolio <Prtfl>", "40.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>", "40.4.15.5.1.15 InvestorTaxReference <InvstrTaxRef>", "40.4.15.5.1.15.1 Type <Tp>", "40.4.15.5.1.15.1.2 Proprietary <Prtry>"]
file_pages: [1548]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.5.1.15.1.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1548 to 1548.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1548

```text
Datatype: "PersonIdentificationType7Code" on page 5341
CodeName Name Definition
ATIN AdoptionTaxpayerIdentificationNumber Temporary tax processing number (used
in the domestic adoption of a child).
GTIN GenericTaxIdentificationNumber Generic tax identification number.
ITIN IndividualTaxpayerIdentificationNumber Tax processing number.
40.4.15.5.1.15.1.2  Proprietary <Prtry>
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
40.4.15.5.1.15.2  Reference <Ref>
Presence: [1..1]
Definition: Pension scheme tax reference issued to the pension plan by a central organisation.
Datatype: "Max35Text" on page 5403
40.4.15.5.1.16  InvestmentsToFollowValue <InvstmtsToFllwVal>
Presence: [0..*]
Definition: Value of the investments to follow.
InvestmentsToFollowValue <InvstmtsToFllwVal> contains the following elements (see
"DateAndAmount2" on page 4343 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Date <Dt> [0..1] Date 4343
   Amount <Amt> [1..1] Amount C2, C10 4343
40.4.15.5.1.17  InnovativeFinance <InnvtvFinc>
Presence: [0..*]
Definition: Information about an innovative finance product.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1548 May 2026
```

