---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12"]
file_pages: [943, 944]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35 sese.012.001.12 PortfolioTransferInstructionV12

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 943 to 944.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 943

```text
35 sese.012.001.12
PortfolioTransferInstructionV12
35.1 MessageDefinition Functionality
Scope
The PortfolioTransferInstruction message is sent by an instructing party, for example, a (new) plan
manager (transferee), to the executing party, for example, a (old) plan manager (transferor), on behalf
of the initiating party, for example, an investor (client), to instruct the transfer of financial instruments
from the client's account at the old plan manager (transferor) to the clients account at the new plan
manager (transferee).
Usage
The PortfolioTransferInstruction message is used to instruct one or more portfolio transfers for one
client. Each portfolio transfer is for delivery to the same account. The account may be owned by one or
more individual investors or one or more corporate investors.
If the instructing party does not have enough information to instruct the portfolio transfer, then it must
first send an AccountHoldingInformationRequest message to the executing party in order to receive an
AccountHoldingInformation message.
Outline
The PortfolioTransferInstructionV12 MessageDefinition is composed of 16 MessageBuildingBlocks:
A. MessageReference
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. PrimaryIndividualInvestor
Information identifying the primary individual investor, for example, name, address, social security
number and date of birth.
F. SecondaryIndividualInvestor
Information identifying the secondary individual investor, for example, name, address, social
security number and date of birth.
G. OtherIndividualInvestor
Information identifying the other individual investors, for example, name, address, social security
number and date of birth.
H. PrimaryCorporateInvestor
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 943 May 2026
```

## File page 944

```text
Information identifying the primary corporate investor, for example, name and address.
I. SecondaryCorporateInvestor
Information identifying the secondary corporate investor, for example, name and address.
J. OtherCorporateInvestor
Information identifying the other corporate investors, for example, name and address.
K. TransferorAccount
Identification of the account owned by the investor at the old plan manager (account servicer).
L. NomineeAccount
Account held in the name of a party that is not the name of the beneficial owner of the shares.
M. Transferee
Identification of the institution to which the financial instrument is to be transferred. This may also
be known as the new plan manager.
N. ProductTransfer
Information about the portfolio and assets.
O. MarketPracticeVersion
Identifies the market practice to which the message conforms.
P. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 944 May 2026
```

