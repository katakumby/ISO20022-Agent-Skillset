---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.1 MessageDefinition Functionality"]
file_pages: [1442, 1443]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1442 to 1443.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1442

```text
39 sese.019.001.09
AccountHoldingInformationRequestV09
39.1 MessageDefinition Functionality
Scope
The AccountHoldingInformationRequest message is sent by an instructing party, for example, a (new)
plan manager (transferee), to the executing party, for example, a (old) plan manager (transferor), on
behalf of the initiating party, for example, an investor (client), to request information about financial
instruments held on behalf of the client.
Usage
The AccountHoldingInformationRequest message is used to request information about assets held on
behalf of the client for which it intends to instruct a portfolio transfer at a later time.
Outline
The AccountHoldingInformationRequestV09 MessageDefinition is composed of 17
MessageBuildingBlocks:
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
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1442 May 2026
```

## File page 1443

```text
J. SecondaryCorporateInvestor
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
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1443 May 2026
```

