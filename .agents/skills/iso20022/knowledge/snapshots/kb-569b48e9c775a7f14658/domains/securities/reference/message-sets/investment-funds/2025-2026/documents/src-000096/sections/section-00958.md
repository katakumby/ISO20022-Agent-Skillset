---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.1 MessageDefinition Functionality"]
file_pages: [1308, 1309]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1308 to 1309.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1308

```text
38 sese.018.001.10
AccountHoldingInformationV10
38.1 MessageDefinition Functionality
Scope
The AccountHoldingInformation message is sent by an executing party, for example, a (old) plan
manager (transferor), to the instructing party, for example, a (new) plan manager (transferee), to
provide information about financial instruments held on behalf of a client.
Usage
The AccountHoldingInformation message is used to provide information on the individual assets held in
a client's account. The assets may be part of a tax efficient product, a pension of general investment
product.
Outline
The AccountHoldingInformationV10 MessageDefinition is composed of 17 MessageBuildingBlocks:
A. MessageReference
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. BusinessFlowDirectionType
Business flow direction (assets to be delivered or received).
F. PrimaryIndividualInvestor
Information identifying the primary individual investor, for example, name, address, social security
number and date of birth.
G. SecondaryIndividualInvestor
Information identifying the secondary individual investor, for example, name, address, social
security number and date of birth.
H. OtherIndividualInvestor
Information identifying the other individual investors, for example, name, address, social security
number and date of birth.
I. PrimaryCorporateInvestor
Information identifying the primary corporate investor, for example, name and address.
J. SecondaryCorporateInvestor
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1308 May 2026
```

## File page 1309

```text
Information identifying the secondary corporate investor, for example, name and address.
K. OtherCorporateInvestor
Information identifying the other corporate investors, for example, name and address.
L. TransferorAccount
Identification of the account owned by the investor at the old plan manager (account servicer).
M. NomineeAccount
Account held in the name of a party that is not the name of the beneficial owner of the shares.
N. Transferee
Identification of the institution to which the financial instrument is to be transferred. This may also
be known as the new plan manager.
O. ProductTransfer
Information about the portfolio and assets.
P. MarketPracticeVersion
Identifies the market practice to which the message conforms.
Q. Extension
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1309 May 2026
```

